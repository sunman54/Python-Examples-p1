from time import sleep as wait
import sys

counter = 0
while True:
    counter += 1

    print("\r Counter : " + str(counter), end='')
    sys.stdout.flush()
    
    wait(0.8)
