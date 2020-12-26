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

#values intercepted from Alice using 'nc socket.cryptohack.org 13371'



p=0xe5a534ad162a08eaee5bd9c165e0b637d57bae0211a531b7ccba0a5d04a2c0d65c0545619a4c685ba77f5c3978d42e8362616c45da9aea18c5117dcb2086b3fb
g=0x02
A=0xad5d6980e68df3ec6ded104f60d9d0fc5bdf62a4c511c55000641ac8d32fd39cdccb509d81d607449e13b58574ac05f7433d94b9e93bda12e3d06fcaf25e4978
#You then generate your secret integer and calculate your public one, which you send to Alice.

b=0x009fdb8b8a004544f0045f1737d0ba2e0b274cdf1a9f588218fb435316a16e374171fd19d8d8f37c39bf863fd60e3e300680a3030c6e4c3757d08f70e6aa871033
b= 0x00da583c16d9852289d0e4af756f4cca92dd4be533b804fb0fed94ef9c8a4403ed574650d3699db29d776276ba2d3d412e218f4dd1e084cf6d8003e7c4774e833
B = pow(g,b,p)

print("B = {}".format(hex(B)))

shared_secret = pow(A,b,p)
print(shared_secret)

#iv and ciphertext intercepted from Alice
#Intercepted from Alice: {"iv": "b0a6ae725c4a16a2233e6cecbde73ee2", "encrypted_flag": "7a476f1fe78ca9715f427f6c6e87aa3f6f962997138571ac4177187235d2e62b"}
iv='0c84c1350d4adcded723fd0e4c37fc6c'
encrypted_flag='81258e3c90dbbc353be5bdd74258a0c408a08525dec686799b3ba2229f4e2dc7'


print(decrypt_flag(shared_secret, iv, encrypted_flag))
