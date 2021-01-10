import requests
import string


def encrypt(b):
    ct = requests.get(f"http://aes.cryptohack.org/ecb_oracle/encrypt/" + b.hex())
    return bytes.fromhex(ct.json()["ciphertext"])


#get the unicode for the characters
ucd = [ord(c) for c in '{_}'+string.printable]


def knownpt(i, prefix=b""):

    #which half
    if 15 - i > 0:
        expected = encrypt(b"a" * (15 - i))[:16]
    else:
        expected = encrypt(b"a" * (31 - i))[16:32]

    #bruteforce the next character
    for c in ucd:
        if 15 - i > 0:
            b = b"a" * (15 - i) + prefix + bytes([c])
            if encrypt(b)[:16] == expected:
                return bytes([c])
        else:
            b = b"a" * (31 - i) + prefix + bytes([c])
            if encrypt(b)[16:32] == expected:
                return bytes([c])



# flag is of format crypto{XXX}. So, take the fixed part and brute force each other character.

pt = b"crypto{"
for i in range(len(pt), 32):
    end = knownpt(i, pt) #keep iterating one at a time till we get }
    pt = pt + end 
    print(pt)
    if end == b"}":
        break