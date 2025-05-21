#!/usr/bin/python3

import sys
import os
import argparse
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description="* CryptX - Encryption tool *")
parser.add_argument("-e", "--encrypt", metavar="PATH", help="Encrypt file|directory")
parser.add_argument("-d", "--decrypt", metavar="PATH", help="Decrypt file|directory")
parser.add_argument("-k", "--key", metavar="KEY", help="Insert encryption/decryption key")
parser.add_argument("-g", "--generate", metavar="KEY", help="Generate encryption key")
parser.add_argument("--version", action="store_true", help="Print program version and exit")
args = parser.parse_args()

extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".txt", ".rtf", ".doc", ".docx", ".odt", \
              ".csv", ".xls", ".xlsx", ".odf", ".ppt", ".pptx", ".odp", ".pdf", ".mp3", ".wma", \
              ".mp4", ".avi", ".mkv"]


def main():
    if args.version:
        sys.exit("CryptX 2.1")
    banner()
    if len(sys.argv) == 1:
        usage()
        sys.exit()
    else:
        if args.key:
            key = get_key()
        elif args.generate:
            if args.decrypt:
                sys.exit("Error: Key Generation Not Supported For Decryption!")
            else:
                key_name = args.generate
                if key_name.endswith(".key"):
                    key_name = key_name.strip(".key")
                key = key_generator(key_name)
        if args.encrypt:
            if not os.path.exists(args.encrypt):
                sys.exit("Error: Path Does Not Exist!")
            if os.path.isfile(args.encrypt):
                unencrypted_file = args.encrypt
                file_encrypt(unencrypted_file, key)
            elif os.path.isdir(args.encrypt):
                unencrypted_dir = args.encrypt
                directory_encrypt(unencrypted_dir, key)
        elif args.decrypt:
            if not os.path.exists(args.decrypt):
                sys.exit("Error: File Does Not Exist!")
            if os.path.isfile(args.decrypt):
                encrypted_file = args.decrypt
                file_decrypt(encrypted_file, key)
            elif os.path.isdir(args.decrypt):
                encrypted_dir = args.decrypt
                directory_decrypt(encrypted_dir, key)


def banner():
    print(
        """
        [ *** CryptX 2.1 *** ]
        ----------------------
        (c)2023 Ivaylo Vasilev
        """
    )


def usage():
    print(
        f"""
        [usage]
        -e, --encrypt  [file|directory] --> encrypt a file
        -d, --decrypt  [file|directory] --> decrypt a file
        -k, --key      [key]            --> specify key
        -g, --generate [key]            --> generate key
        --version                       --> print version
        -h, --help                      --> print help

        [example]
        {sys.argv[0]} -e filename.txt -k keyname.key
        {sys.argv[0]} -e filename.txt -g keyname
        {sys.argv[0]} -d filename.txt -k keyname.key
        {sys.argv[0]} -e directory -k keyname.key
        {sys.argv[0]} -e directory -g keyname
        {sys.argv[0]} -d directory -k keyname.key
        
        [supported file extensions]
        .jpg * .jpeg * .png * .bmp * .gif * .txt * .rtf
        .doc * .docx * .odt * .csv * .xls * .xlsx * .odf
        .ppt * .pptx * .odp * .pdf * .mp3 * .wma * .mp4"
        .avi * .mkv

        """
    )


def get_key():
    try:
        if not os.path.exists(args.key):
            sys.exit("WARNING! Key Not Found!")
        else:
            keyfile = args.key
    except:
        sys.exit("Error: Missing option -k or --key!")
    with open(keyfile, "rb") as key:
        secret_key = key.read()
    return secret_key


def key_generator(filename):
    secret_key = Fernet.generate_key()
    with open(f"{filename}.key", "wb") as file:
        file.write(secret_key)
    print("[ OK ] Secret key generated!")
    return secret_key


def file_encrypt(file, key):
    print(f"Encrypting {file} ...", end="\r")
    with open(file, "rb") as f:
        unencrypted_file = f.read()
    encrypted_file = Fernet(key).encrypt(unencrypted_file)
    with open(file, "wb") as e:
        e.write(encrypted_file)
    print(f"Encrypting {file} ... done")


def file_decrypt(file, key):
    print(f"Decrypting {file} ...", end="\r")
    with open(file, "rb") as e:
        encrypted_file = e.read()
    try:
        decrypted_file = Fernet(key).decrypt(encrypted_file)
    except:
        sys.exit("Error: Decryption Failed! Invalid key!")
    with open(file, "wb") as f:
        f.write(decrypted_file)
    print(f"Decrypting {file} ... done")


def directory_encrypt(path, key):
    print("Encrypting directory ...")
    for root, directory, files in os.walk(path):
        for file in files:
            for e in extensions:
                if file.endswith(e):
                    try:
                        fullfile = os.path.join(root, file)
                        with open(fullfile, "rb") as f:
                            unencrypted_file = f.read()
                        encrypted_file = Fernet(key).encrypt(unencrypted_file)
                        with open(fullfile, "wb") as e:
                            e.write(encrypted_file)
                        print(f"[ OK ] Successfully Encrypted: {file}")
                    except:
                        print(f"[ FAILED ] Could Not Encrypt: {file}")


def directory_decrypt(path, key):
    print("Decrypting ...")
    for root, directory, files in os.walk(path):
        for file in files:
            for e in extensions:
                if file.endswith(e):
                    try:
                        fullfile = os.path.join(root, file)
                        with open(fullfile, "rb") as e:
                            encrypted_file = e.read()
                        decrypted_file = Fernet(key).decrypt(encrypted_file)
                        with open(fullfile, "wb") as f:
                            f.write(decrypted_file)
                        print(f"[ OK ] Successfully Decrypted: {file}")
                    except:
                        print(f"[ FAILED ] Could Not Decrypt: {file}")


if __name__ == "__main__":
    main()
