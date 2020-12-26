from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import pwn
import json
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

#values intercepted from Alice using 'nc socket.cryptohack.org 13371'

remote = pwn.remote("socket.cryptohack.org",13371)
remote.recvuntil("Intercepted from Alice: ")
frm_alice = json.loads(remote.recvline())
frm_alice['p'] = "1"
remote.recvuntil("Send to Bob: ")
remote.sendline(json.dumps(frm_alice))

remote.recvuntil("Intercepted from Bob: ")
remote.sendline(remote.recvline())

remote.recvuntil("Intercepted from Alice: ")
alice_cyphertext = json.loads(remote.readline())

shared_secret = 0


print(decrypt_flag(shared_secret, alice_cyphertext["iv"], alice_cyphertext["encrypted_flag"]))
