import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0,)
        connection.settimeout(5)
    except socket.error as error:
        print("Error creating socket: {}".format(error))
        sys.exit()
    print("Socket created")

    target_host = input("Enter host to connect to: ")
    target_port = int(input("Enter port to connect to: "))

    try:
        connection.connect((target_host, target_port))
        print('TCP client successfuly connectected')
        connection.shutdown(2)
    except socket.error as error:
        print("Error: {}".format(error))
        sys.exit()


if __name__ == '__main__':
    main()
