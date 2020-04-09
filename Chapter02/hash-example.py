# -*- coding: utf-8 -*-
import hashlib

md  = hashlib.md5()
sha = hashlib.sha256()

# md5 Uppercase first letters
md.update("Hello World".encode('utf-8'))
print (md.hexdigest())

# md5 Lowercase first letters
md.update("hello world".encode('utf-8'))
print (md.hexdigest())

# sha Uppercase first letters
sha.update("Hello World".encode('utf-8'))
print (sha.hexdigest())

# sha Lowercase first letters
sha.update("hello world".encode('utf-8'))
print (sha.hexdigest())

