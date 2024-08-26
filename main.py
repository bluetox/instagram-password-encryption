import json
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from nacl.public import SealedBox, PublicKey


def r(a, b):
    public_key = PublicKey(b)
    sealed_box = SealedBox(public_key)
    encrypted_message = sealed_box.encrypt(a)
    return encrypted_message


def aes_gcm_encrypt(password: str, timestamp: int):
    key = os.urandom(32)
    iv = os.urandom(12)
    additional_data = str(timestamp).encode()
    tag_len = 16

    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=None
    ).encryptor()

    encryptor.authenticate_additional_data(additional_data)
    ciphertext = encryptor.update(password.encode()) + encryptor.finalize()

    return {
        "ciphertext": ciphertext,
        "iv": iv,
        "tag": encryptor.tag,
        "key": key
    }

# Load data from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

password = config["password"]
timestamp = config["timestamp"]
public_key_hex = config["public_key_hex"]

result = aes_gcm_encrypt(password, timestamp)
t = bytes.fromhex(public_key_hex)
b = r(result["key"], t)
u = bytearray()
u.extend([1, 198])
u.extend([80])
u.extend([0])
u.extend(b)
b = result["tag"] + result["ciphertext"]
a = b[-16:]
b = b[:len(b)-16]
u.extend(a)
u.extend(b)
encodedpassword = base64.b64encode(u)
print(f"#PWD_INSTAGRAM_BROWSER:10:{timestamp}:{encodedpassword.decode('utf-8')}")
