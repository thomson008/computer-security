from Crypto.Hash import SHA1
from collections import Counter

passwords = ['123456', '12345', '123456789', 'password', 'iloveyou', 'princess', '1234567',
   'rockyou', '12345678', 'abc123', 'nicole', 'daniel', 'babygirl', 'monkey', 'lovely', 'jessica',
      '654321', 'michael', 'ashley', 'qwerty', '111111', 'iloveu', '000000', 'michelle', 'tigger']

samples = open("rockyou-samples.sha1-salt.txt")
counts = Counter()

print('Checking all hashes...')
for line in samples.readlines():
    elements = line.split('$')
    salt = elements[2]
    hashed = elements[3][:-1]
    
    for password in passwords:
        concat = salt + password
        if SHA1.new(bytearray(concat, 'utf-8')).hexdigest() == hashed:
            counts.update({password : 1})

print('Writing file...')
with open('salt-cracked.txt', 'w') as cracked:
    for password, count in counts.items():
        row = str(count) + ',' + password + '\n'
        cracked.write(row)

print('Done.')