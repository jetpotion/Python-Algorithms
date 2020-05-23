
import numpy as np 
#This will use the forward euler method 
def main():
   #This will increment the time by minutes we will increment by 1 since my k is in terms of minutes 
    h = 1;
    #We can calculate the time before he died
     
    #This guy died 20.533397 minutes before we found the body We calculate via the given K 
    deltabeforedeath =  np.log((np.power(91.11, 0.999)- 34.44) / (np.power(97.88,0.999) -34.44)) /  -0.005504671;
    print(deltabeforedeath)

   #This means this guy died at this time 11:39.466603 
    print("This guy died at " + str(11) + ":" +  str(39.466603) ) 
   #Now we everything to calculate for when this guy will reach 55.55 degrees
    initialtemperature = 97.88
    initialtime  = 0
    #Now we perform the newton euler method and will  take a walk across the solution of the differential equation till we get a number close to 44.44
    while initialtemperature  >= 44.44:
        print("Temperature: " + str(initialtemperature) +" " +"time: " +   str(initialtime))
        initialtime += h 
        initialtemperature += h *   newtonlawofcooling(initialtime,initialtemperature)
    
    print("The amount of time till the body reaches 44.44 from a body temperature of 97.88: "  +str(initialtime)+ "minutes")
#Temperature of death
#We need to find the time we died 


def newtonlawofcooling(time,temperature):
    #Solving for the DE we simply only need to raise the temperature to the 0.999 power
    #Solving for the rate of cooling per minute we have constant cooling factor and we solve into terms of minutes. 
    
    return -0.0055046671 * (np.power(temperature,0.999) - 34.44);
if __name__ == "__main__":
    main()

