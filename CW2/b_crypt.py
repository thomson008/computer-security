from bcrypt import hashpw, gensalt, checkpw

occurences = []
password = b'123456'
samples = open('rockyou-samples.bcrypt.txt', 'r')

i = 1
for hashed in samples.readlines():
    if (checkpw(password, hashed[:-1].encode())):
        occurences.append(i)
    i += 1
    if len(occurences) == 5:
        break

with open('bcrypt-lines.txt', 'w') as lines:
    lines.write(str(occurences))



