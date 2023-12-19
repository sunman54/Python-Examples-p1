from time import sleep as wait

counter = 0
while True:
    counter += 1

    print("\r Counter : " + str(counter), end='')
    
    wait(0.8)
