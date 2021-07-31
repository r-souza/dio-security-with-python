import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as error:
        print('Error creating socket: {}'.format(error))
        sys.exit()
    print('Socket created')

    host = '127.0.0.1'
    port = 5433

    message = 'Server: Hello Client'

    try:
        connection.bind((host, port))
    except socket.error as error:
        print('Error binding socket: {}'.format(error))
        sys.exit()

    while True:
        data, address = connection.recvfrom(4096)
        print('Server: Message received from {}'.format(address))

        if data:
            print('Message received: {}'.format(data))
            connection.sendto(data + (message.encode()), address)


if __name__ == '__main__':
    main()
