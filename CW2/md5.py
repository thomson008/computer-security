from Crypto.Hash import MD5
from collections import Counter

f = open('rockyou-samples.md5.txt', 'r')

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2' '3', '4', '5', '6', '7', '8', '9']

mapping = {}
counts = Counter()

for i in chars:
    for j in chars:
        for k in chars:
            for l in chars:
                for m in chars:
                    password = ''.join([i, j, k, l, m])
                    hashed = MD5.new(str.encode(password)).hexdigest()
                    mapping[hashed] = password

with open('mappings.txt', 'w') as maps:
    maps.write(str(mapping))


for hash_code in f.readlines():
    if hash_code in mapping.keys():
        password = mapping[hash_code[:-1]]
        counts.update({password : 1})


with open('md5-cracked.txt', 'w') as cracked:
    for password, count in counts.items():
        row = str(count) + ',' + password + '\n'
        cracked.write(row)

    
