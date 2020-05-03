crypto - cryptography CLI application
=====================================

Description
-----------
**crypto** is a Linux Python3 CLI program for generating encryption/decryption keys, encrypting files, creating digital envelopes, digital signatures, and digital seals (digitally signed digital envelopes). 
    
It consists of two source files, crypto and CryptoData.py. crypto is the main executable and CryptoData.py defines the class that describes cryptographic data such as keys, envelopes, and others, in a unified format and also allows reading from and writing to files in a human-readable text format.

Dependencies
------------
* [cryptography] - cryptography algorithms implementation

Use
---
Crypto creates files in the same directory where the input files are located.
Here are a few examples of how to use the program:

* See the full help message that shows you all the details on the parameters of the program:    

`crypto -h` or `crypto --help`

* Generate a secret key for _AES_ of size 256 bits with the _CTR_ mode of encryption:

`crypto -s AES -S 256 -m CTR create secret key_prefix`

* Generate an RSA public and private key pair with a modulus of size 2048 bits, and with the public exponent _e = 65537_:

`crypto -a RSA -e 65537 create public key_prefix`

* Encrypt a file using _TripleDES_ symmetric encryption in _CBC_ mode with an automatically generated secret key of size 192 bits:

`crypto -s TripleDES -S 192 -m CBC create symmetric plaintext_file.txt`

* Decrypt a file using asymmetric encryption with a private key:

`crypto -p private_key.x read asymmetric encrypted_file.x`

* Create a digital envelope with the receiver's public key and an automatically generated secret key:

`crypto -P public_key.x create envelope plaintext_file.txt`

* Verify a digitally signed file with the sender's public key (this requires that the original file is in the same directory as the signature file):

`crypto -P public_key.x read signature signature_file.x`

* Create a digital seal with the sender's private key and receiver's public key:

`crypto -p sender_private_key.x -P receiver_public_key.x create seal plaintext_file.txt`

_Note: if you do not add the directory in which Crypto is located to your PATH variable, you will need to specify the full path to Crypto (relative or absolute). Instead of simply writing `crypto`, you will write `path_to_crypto/crypto`. Or you can run it using Python3 as `python3 path_to_crypto/crypto`._

  [cryptography]: <https://pypi.org/project/cryptography/>
