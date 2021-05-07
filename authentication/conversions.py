import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]
credentials = {}
for line in open('passwords.txt'):
    split_line = line.split(':')
    credentials[split_line[1]] = split_line[0]
passwords_cracked = 0
hashes_computed = 0
pw_file = open('passwords1.txt','w')

for word in words:
    encoded_attempt = word.encode('utf-8')
    md5 = hashlib.md5(encoded_attempt)
    hash = md5.digest()
    hashes_computed += 1
    hexed_hash = binascii.hexlify(hash)
    string_hash = hexed_hash.decode('utf-8')
    for hashed_password in credentials:
        if string_hash == hashed_password:
            passwords_cracked += 1
            pw_file.write(credentials[hashed_password] + ':' + word + '\n')
            break

pw_file.close()
pw_per_hash = passwords_cracked / hashes_computed
print('Passwords cracked: {}'.format(passwords_cracked))
print('Hashes computed: {}'.format(hashes_computed))
print('Passwords cracked per hash computed: {}'.format(pw_per_hash))
