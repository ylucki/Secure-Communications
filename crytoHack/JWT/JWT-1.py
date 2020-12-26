import jwt

print(jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ', verify=False))
print(jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOmZhbHNlfQ.yRhbtEnBab1UfHM95yP6Ukz3EQrQqP6lwZFcqwvKwjg', verify=False))

encoded_jwt = jwt.encode({'username': 'admin', 'admin': True}, 'secret', algorithm='HS256')
print(encoded_jwt)




pubkey="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsXRBeaADq9e5tKU5UzAc\n/Ty4e/kUmIMJJXeIYBy8qs9mfB2OISHIRLZj7jqxuhqa+bi6VNhIEGUdvOBQYGnZ\nHoTGKsMDTjAiWVC7AQUVirLt1oZDNat+7hs5lnkscpx4B5tSEFR0C5uC9cDoolrZ\nP366Bykb1nYfp7B8JIZS1iYgT6WWYO+aZ3/z95vJku1XiYSCbwGxntkP0w0bOBth\nKBfUIFHHa53ba6l8GT6ATAYA0hak8FTz7on+GQme0GYUV1DpnZ4Rx8x8/jWK49w/\n70/OxCKCYzXhYt/5tB2SweRUOsVSHYtpLa6ad0J4xydkmJaGshvYrHT5+Uk0zFHK\npwIDAQAB\n-----END PUBLIC KEY-----\n"

from Crypto.PublicKey import RSA

rsakey = RSA.import_key(pubkey)
print("Key Size (bytes): ", rsakey.size_in_bytes())
print("rsa key parameters: ", rsakey.__dict__)
print("Private key: ", rsakey._n)
d=rsakey._n

encoded_jwt = jwt.encode({'username': 'admin', 'admin': True}, key=d, algorithm='HS256' )