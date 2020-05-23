"@author: William Zhang"
"@email:William.Zhang@Stonybrook.edu"
import numpy as np 
def main():
    vinitial = 300;
    #The time jump will be  1s
    timejump = 0.001;
    timeinitial = 0
    totaldistancetraveled = 0 
    #We will check the time it takes to reach zero velocity 
    #Apply forward newton forward method as necessary as long velocity is greater than or equal to zero
    while( vinitial + timejump * bulletup(timeinitial,vinitial) >= 0 ):
        print("The current time: " + str(timeinitial) + " Velocity:" + str(vinitial))
        timeinitial += timejump
        totaldistancetraveled += timejump  *  vinitial
        vinitial += timejump * bulletup(timeinitial,vinitial) 
    down = 0 
    while(down  < totaldistancetraveled):
        print("The current time: " + str(timeinitial) + "Velocity: " + str(vinitial ))
        timeinitial += timejump
        vinitial +=  timejump * bulletdown(timeinitial,vinitial)
        down +=  timejump * vinitial
    totaldistancetraveled *= 2
    
    #Find a way to calculate distance
    print("Total distance it was in the air " + str(totaldistancetraveled))
    print("Total time bullet was in air: " + str(timeinitial))
def bulletup(time,velocity):
    return -9.8  - (0.00911 * np.power(velocity,0.999))/0.1
def bulletdown(time,velocity):
    return 9.8 -  0.00911 * np.power(velocity,0.999)
if __name__ == "__main__":
    main() 


