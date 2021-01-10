from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import bytes_to_long, long_to_bytes



def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))

    key = sha1.digest()[:16]

    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    print("plaintext: {}".format(plaintext))

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

#values intercepted from Alice using 'nc socket.cryptohack.org 13379'

"""
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported": ["DH64"]}
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x4e24f4cd6fbe82f0"}
Intercepted from Bob: {"B": "0x2493ce6143871fa0"}
Intercepted from Alice: {"iv": "45330295c2d083c402d31a18a18ad0e6", "encrypted_flag": "498677d3d0f24a9464149e3dc9eb29d5c9a3d2f5c1c2682a1b84a527e7ec1baa"}

"""


p = 0xde26ab651b92a129
g = 0x2
A = 0x4e24f4cd6fbe82f0
B = 0x2493ce6143871fa0

iv = "45330295c2d083c402d31a18a18ad0e6"
encrypted_flag = "498677d3d0f24a9464149e3dc9eb29d5c9a3d2f5c1c2682a1b84a527e7ec1baa"





