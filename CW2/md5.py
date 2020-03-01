from Crypto.Hash import MD5
from collections import Counter
from itertools import product
import string

f = open('rockyou-samples.md5.txt', 'r')

chars = string.digits + string.ascii_lowercase
mapping = {}
counts = Counter()

for combination in product(chars, repeat=5):
    password = ''.join(combination)
    hashed = MD5.new(bytearray(password, 'utf-8')).hexdigest()
    mapping[hashed] = password

for hash_code in f.readlines():
    if hash_code[:-1] in mapping:
        password = mapping[hash_code[:-1]]
        counts.update({password : 1})

with open('md5-cracked2.txt', 'w') as cracked:
    for password, count in counts.items():
        row = str(count) + ',' + password + '\n'
        cracked.write(row)

    
