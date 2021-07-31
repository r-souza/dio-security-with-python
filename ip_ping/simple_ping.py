import os

print('#' * 80)
host = input("Enter host to ping: ")
print('-' * 80)

os.system('ping -c 6 {}'.format(host))
print('-' * 80)
