#!/usr/lib/bin python3

from Crypto.Cipher import AES
import hashlib
import random
import binascii

def block_cipher_mode_starter():
    #{"plaintext":"63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d"}
    pass

# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words

with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
#FLAG = ?


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
        result = binascii.unhexlify(decrypted.hex())
        if result.startswith('crypto{'.encode()):
            print(result.decode('utf-8'))
             
    except ValueError as e:
        return {"error": str(e)}

    return {decrypted.hex()}


#@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}

def password_as_keys():
    cipher_text = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

    with open("/usr/share/dict/words") as f:
        words = [w.strip() for w in f.readlines()]
        for keyword in words:
            password_hash = hashlib.md5(keyword.encode()).digest().hex()
            plaintext = decrypt(cipher_text,password_hash)


    

def ecb_oracle():
    cipher_text1 = '9931fba2162ac1a3512f046baa6e39757a74e7f2d5267f1ef525d57e1144a38f3c3a5a67f9e0d7c80915f1b8d04c304f'
    cipher_text2 = '760f98908bf7680f99489814bf6c285d7a74e7f2d5267f1ef525d57e1144a38f3c3a5a67f9e0d7c80915f1b8d04c304f'
    

def main():
    password_as_keys()

if __name__ == "__main__":
    main()
