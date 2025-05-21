#!/usr/bin/python3

import sys
import argparse
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description="* CryptX Key Generator *")
parser.add_argument("-k", "--key", metavar="KEYNAME", default="secret-key", help="Specify key name")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        sys.exit(f"[usage] {sys.argv[0]} -k [--key] KEYNAME")
    else:
        secret_key = args.key
        if secret_key.endswith(".key"):
            secret_key = secret_key.strip(".key")
        key_generator(secret_key)


def key_generator(filename):
    key = Fernet.generate_key()
    with open(f"{filename}.key", "wb") as file:
        file.write(key)
    print("[+] Secret key generated!")


if __name__ == "__main__":
    main()
