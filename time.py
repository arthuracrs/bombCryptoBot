import datetime
from time import sleep

current = datetime.datetime.now()
print(current)

sleep(10)
print((datetime.datetime.now() - current).seconds)