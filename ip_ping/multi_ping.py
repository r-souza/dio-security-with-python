import os
import time

with open('hosts.txt') as file:
    # dump = file.read()
    # for host in dump.split('\n'):
    dump = file.read().splitlines()

    for host in dump:
        if host:
            print('-' * 80)
            os.system('ping -c 2 {}'.format(host))
            print('-' * 80)

            time.sleep(2)
