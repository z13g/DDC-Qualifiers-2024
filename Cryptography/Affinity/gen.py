#!/usr/bin/env python
from math import gcd
import random
import binascii

# Encrypt the text using the affine cipher y = (ax + b) mod m
def affine_encrypt(text, a, b, m):
    result = 0
    for letter in text:
        c = (a * letter + b) % m
        result = (result << 8) + c
    return hex(result)

# Generate keys for the affine cipher and encrypt the flag
if __name__ == '__main__':
    with open('flag.txt', 'rb') as file:
        plaintext = file.read().strip(b'\n')

    m = 256
    a = random.randint(1, m)
    while gcd(a, m) != 1:
        a = random.randint(1, m)
    b = random.randint(0, m)

    print(f'Key = {(a, b)}')
    ciphertext = affine_encrypt(plaintext, a, b, m)

    with open('output.txt', 'w') as file:
        file.write(ciphertext)
