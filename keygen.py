#!/usr/bin/env python3

import sys
import argparse
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description="* CryptX Key Generator *", epilog="(c)Ivaylo Vasilev")
parser.add_argument("-k", "--key", metavar="KEYNAME", default="secret", help="key name")
parser.add_argument("--version", action="version", version="CryptX Key Generator 1.1")
args = parser.parse_args()


def main():
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
