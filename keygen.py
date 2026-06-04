#!/usr/bin/env python3

##############################
# CryptX Key Generator #
# ==================== #
# Tool to generate Fernet security keys
# Copyright (c)2025 Ivaylo Vasilev. Released under the MIT License; see LICENSE for details.
# Author: Ivaylo Vasilev
##############################

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
