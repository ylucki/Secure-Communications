#!/usr/bin/env python3
#Part 1 - ASCII
l = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49,110, 116, 52, 98, 108, 51, 125]
m = ''
for letter in l:m += chr(letter)
print('General Encoding 1: ' + m)

etxt = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print('Ascii txt: ' + bytearray.fromhex(etxt).decode())


#Part 3 - Base 64

"""Convert Hex string to Base64"""
import base64

HEX_STRING = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

BYTE_ARRAY = bytearray.fromhex(HEX_STRING)
print(BYTE_ARRAY)
BASE64_VAL = base64.b64encode(BYTE_ARRAY)
print(BASE64_VAL)


#Part 4 - long to bytes

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

lint=11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(lint)
print(bytes)
