import hashlib

available_methods  = [
    {'number': 1, 'description': 'md5'},
    {'number': 2, 'description': 'sha1'},
    {'number': 3, 'description': 'sha256'},
    {'number': 4, 'description': 'sha512'}
]

def show_menu():
    print(''' Welcome to the hash generator.

    The following hash algorithms are available:
    ''')

    for method in available_methods:
        print('{}. {}'.format(method['number'], method['description']))


def generate_hash(text, method):

    hash = hashlib.new(method)

    result = hash.update(text.encode('utf-8'))

    print("""\nThe {} hash for "{}" is: {} \n""".format(method, text, hash.hexdigest()))

def main():
    show_menu()

    method = int(input('\nPlease select a hash method: '))
    text = input('Please enter the text to be hashed: ' )

    generate_hash(text, available_methods[method-1]['description'])


if __name__ == '__main__':
    main()
