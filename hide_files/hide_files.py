import ctypes

hidden_attribute = 0x02

result = ctypes.windll.kernel32.SetFileAttributesW(
    'hidden.txt', hidden_attribute)

if result:
    print('Set hidden attribute for hidden.txt')
else:
    print('Failed to set hidden attribute for hidden.txt')
