import hashlib

file_a = 'hash_compare_a.txt'
file_b = 'hash_compare_b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file_a, 'rb').read())
print('Hash for file_a: {}'.format(hash1.hexdigest()))

hash2 = hashlib.new('ripemd160')
hash2.update(open(file_b, 'rb').read())
print('Hash for file_b: {}'.format(hash2.hexdigest()))


if (hash1.digest() != hash2.digest()):
    print("The files are different.")
else:
    print("The files are the same.")