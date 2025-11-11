# CryptX
Encrypt / Decrypt files
---
**CryptX** is a CLI program written in **Python** to encrypt and decrypt files. It uses a ***cryptography*** library and a Fernet 256-bit key to encrypt and decrypt files of given extensions.

**Note:** Keep the generated key secure, as anyone with access to it ***can*** decrypt the encrypted files! Be aware, that if you ***loose access*** to the secret key your files will remain encrypted!


**Supported file types for encryption:** .jpg .jpeg .png .bmp .gif .txt .rtf .doc .docx .odt .csv .xls .xlsx .odf .ppt .pptx .odp .pdf .mp3 .wma .mp4 .avi .mkv


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



**Keygen** is a small tool to generate Fernet security keys.


**keygen.py**
```
$ keygen.py --help
usage: keygen.py [-h] [-k KEYNAME]

* CryptX Key Generator *

options:
  -h, --help         show this help message and exit
  -k, --key KEYNAME  Specify key name
```
