import itertools

string = input("Enter string to permute: ")
result = itertools.permutations(string, len(string))

for char in result:
    print(''.join(char))