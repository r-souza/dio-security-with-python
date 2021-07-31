import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connection.settimeout(5)
    except socket.error as error:
        print('Error creating socket: {}'.format(error))
        sys.exit()
    print('Socket created')

    host = '127.0.0.1'
    port = 5433

    message = 'Client: Hello Server \n'

    try:
        print('Sending message: {} \n'.format(message))
        connection.sendto(message.encode(), (host, port))

        data, address = connection.recvfrom(4096)

        data = data.decode()

        print('{}'.format(data))
    finally:
        print('Closing socket')
        connection.close()


if __name__ == '__main__':
    main()
