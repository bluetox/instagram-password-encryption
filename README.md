# Instagram Password Encryption Replication (Python)

This project is a Python script that attempts to replicate the client-side encryption used by Instagram for passwords before they are sent to the server. 

## Disclaimer
**Important:** The script is currently not fully compatible with Instagram's encryption due to differences between Instagram's Crypto API and the Python `cryptography` library. This project is intended for educational purposes only.

## Features
- Mimics the client-side password encryption used by Instagram.
- Uses the Python `cryptography` library to replicate the encryption process.

## Limitations
- **Compatibility:** The encryption method is not fully compatible with Instagram's client-side encryption due to differences between the Crypto API and the Python `cryptography` library.
- **For Educational Purposes Only:** This project is intended for understanding and experimentation with encryption processes, not for use in production environments.

## Prerequisites
- Python 3.x
- `cryptography` library

To install the required dependencies, run:
```bash
pip install cryptography
