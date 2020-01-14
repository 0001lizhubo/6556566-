#coding=utf-8
from hashlib import sha1
#将密码转换为sha1值返回
def gethash(mima):
    secret=sha1()
    #为了确保密码的安全，需要加salt值，salt值为“2020”
    salt = "2020"
    secret.update((str(mima)+salt).encode('utf-8'))
    secret2=secret.hexdigest()
    print(secret2)
    return secret2
gethash("123456")
gethash("123457")