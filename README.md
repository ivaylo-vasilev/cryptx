# cryptx
Encrypt / Decrypt files
---

**cryptx.py**
```
$ cryptx.py --help
usage: cryptx.py [-h] [-e PATH] [-d PATH] [-k KEY] [-g KEY] [--version]

* CryptX - Encryption tool *

options:
  -h, --help          show this help message and exit
  -e, --encrypt PATH  Encrypt file|directory
  -d, --decrypt PATH  Decrypt file|directory
  -k, --key KEY       Insert encryption/decryption key
  -g, --generate KEY  Generate encryption key
  --version           Print program version and exit
```

**keygen.py**
```
$ keygen.py --help
usage: keygen.py [-h] [-k KEYNAME]

* CryptX Key Generator *

options:
  -h, --help         show this help message and exit
  -k, --key KEYNAME  Specify key name
```
