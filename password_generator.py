import random, string

size = int(input("How many characters do you want your password to be? "))
chars = string.ascii_letters + string.digits + '!@#$%^&*()-_=+'

print(''.join(random.SystemRandom().choice(chars) for _ in range(size)))