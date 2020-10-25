#!/usr/bin/env python3

from pwn import xor
from binascii import unhexlify
from Crypto.Util.number import long_to_bytes

import base64

KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
b = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

#KEY2 = xor(bytearray.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'), bytearray.fromhex(KEY1))
KEY2 =  KEY1 ^ b
print("[-] KEY2: {}".format(KEY2))

KEY3 = xor("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", KEY2)
print("[-] KEY3: {}".format(KEY3))

KEY4 = xor(xor(KEY1, KEY2), KEY3)
print("[-] KEY4: {}\n".format(KEY4))

FLAG = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", KEY4)
print("[*] FLAG: {}".format(FLAG))
#print("[*] FLAG: {}".format(unhexlify(FLAG)))
print("[*] FLAG: {}".format(long_to_bytes(FLAG)))


#b = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
#>>> key1 = a
#>>> key2 = a ^ b 
#>>> key3 = key2 ^ c
#>>> flag = d ^ key1 ^ key2 ^ key3
#>>> long_to_bytes(flag)
#b'crypto{x0r_i5_ass0c1at1v3}'
