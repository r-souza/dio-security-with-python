from threading import Thread
import time

def car(speed, driver):
    km = 0
    while km < 200:
        print('Driver: {} - Km: {} \n'.format(driver, km))
        km += speed
        time.sleep(0.75)

    print('{}km done by driver {} \n'.format(km, driver))

t_john = Thread(target=car, args=(20, 'John'))
t_jane = Thread(target=car, args=(25, 'Jane'))

t_john.start()
t_jane.start() 
    