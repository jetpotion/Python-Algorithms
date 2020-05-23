"@author: William Zhang"
"@email:William.Zhang@Stonybrook.edu"
import numpy as np
from  Needle import Needle 
#This method will call all the other functions
def main():
    pinlength = 1
    pinlength2 = 0.5
    pinlength3  = (1/3)
    pinlength4  = 0.25
    linedistance  = 20 
    probability1 = montecarlo(linedistance,pinlength)
    probability2 = montecarlo(linedistance, pinlength2)
    probability3 = montecarlo(linedistance,pinlength3)
    probability4  = montecarlo(linedistance,pinlength4)
    print("Approximation with a pinlength 1: " + str(probability1)) 
    print("Approximation with a pinlength 0.5: " +str( probability2))
    print("Approximation with a pinlength 0.333:" +str( probability3))
    print("Approximation with a pinlength 0.25: " +str( probability4))
#This will throw the needle randomly
def  throwneedle(length,spacebetween):
    return  length,np.random.uniform(0,spacebetween),np.random.uniform(0,np.pi)

#Check intersections
def checkintersections(center,length,angle,linedistance):
    #Check if the needle is intersecting the right wall 
    if center +  length / 2 * np.sin(angle) >= linedistance :
        return True 
    #Check if the needle is intersecting the left wall 
    elif center + length /2 * np.sin(angle) <= 0:
        return True 
    #THe needle doesnt intersect at all 
    else:
        return False 

def montecarlo(linedistance, pinlength):
    #This will be the number of iterations for  our simulations
    numberofiterations = 3000000
    counter = 0 
    for x in range(numberofiterations):
        #Count the ones that do intersect 
        length,center,angle =  throwneedle(pinlength,linedistance) 
        if(checkintersections(center,length,angle,linedistance)) :
            counter += 1
    return (counter * 100) / (numberofiterations * 100)

if __name__ == "__main__":
    main() 

