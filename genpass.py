#!/usr/bin/env python
# Inspired by https://stackabuse.com/python-check-if-variable-is-a-number/
import sys
import string
import secrets

pass_len = 16

try:
    sys.argv[1]
except IndexError:
    pass
else:
    try:
        pass_len = int(sys.argv[1])
    except ValueError:
        print('Usage: genpass [length:int]')
        sys.exit()

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(pass_len))
print(password)
