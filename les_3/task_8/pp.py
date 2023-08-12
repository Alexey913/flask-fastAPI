import hashlib
import os
 
def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1_000_000)
    print(f'{salt=}')
    print(f'{key=}')
    return key, salt

password = '111111'
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1_000_000)

key_2 = hash_password(password, salt)

print(key)
print(key_2[1])
print(key_2[0])