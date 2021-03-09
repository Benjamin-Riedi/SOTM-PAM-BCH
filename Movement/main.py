from functions import *

while True:
    position = positionrobot()+positionTarget()+ordersCheck()+modeCheck()
    print(time.strftime(" %H: %M: %S:"))
    print(position)