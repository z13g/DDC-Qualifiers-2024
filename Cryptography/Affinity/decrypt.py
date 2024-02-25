#!/usr/bin/env python
from math import gcd
import random

def affine_decrypt(ciphertext, a, b, m):
    decrypted_text = ""
    a_inv = pow(a, -1, m)
    for c in ciphertext:
        x = (a_inv * (c - b)) % m
        decrypted_text += chr(x)
    return decrypted_text

def zieg():
    ciphertext_hex = '0xe9e962ea422bdc1d39965e2b341de5dc260f5050c9b2260f960f016c0f50342b6c39dcf8'
    m = 256
    ciphertext_bytes = bytes.fromhex(ciphertext_hex[2:])
    ciphertext = [ciphertext_bytes[i] for i in range(len(ciphertext_bytes))]
    try_cnt = 0
    while True:     
        a = random.randint(1, m)
        while gcd(a, m) != 1:
            a = random.randint(1, m)
        b = random.randint(0, m)
        decrypted_text = affine_decrypt(ciphertext, a, b, m)
        try_cnt += 1
        if "DDC{" in decrypted_text:
            with open('decrypted.txt', 'w', encoding='utf-8') as file: 
                file.write(decrypted_text)
            print(f"Cipher Hex Decrypted\nKey = {a, b}\nDecrypted text = {decrypted_text}")
            return
        print(f"Try {try_cnt}")

if __name__ == '__main__':
    zieg()
