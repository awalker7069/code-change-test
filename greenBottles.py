#green bottle program using a for loop.
import time
bottles = 10
for bottles in range(bottles,0,-1):
    print("There are {0} green bottles, hanging on a wall, \n{0} green bottles, hanging on a wall ".format(bottles))
    print("And if 1 green bottle should accidentally fall, \nThere'll be {0} green bottles hanging on a wall. \n".format(bottles-1))
    time.sleep(2)
    
