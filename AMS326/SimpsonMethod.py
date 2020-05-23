# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:07:04 2019

@author: William Zhang
"""

import math as math
"We first need to find the function of X and Y. But notice the graph of the function. The function is symmetric across the Y axis."
"This is why we only want the the function that is defined for the positive X. We have to also make the equation in terms of X first but" 
"only want the function that is defined strictly on the positive X domain of the function"

#This first function1 represents the upper half of the heart function of the right half of the function on the graph
def function1(x):
    
        
    return math.sqrt(2 -  x * x) + math.sqrt(x)


#The second function2 represent the bottom half of the heart function of the right half of the function 
def function2(x):
    
    return -(math.sqrt(2- x * x)) + math.sqrt(x)


def main():
     upperighthalf = simpsonmethod1()
     lowerrighthalf = simpsonmethod2()
     righthalf  = upperighthalf + lowerrighthalf
     totalintegral = 2 * righthalf 
     print("The total approximation of the integral is " + str(totalintegral))
     
    
    
    


#Performs the simpson method on the first function. We need to integrate into 2 seperate parts 
def simpsonmethod1():
    #This will be the number of strips to use 
    n = 4000
    
    #This will be the interval  from [a,b] since the function is only defined from 0 to sqrt(2)
    endpoint = 1.41421356237
    startingpoint = 0.00
    
    #This will be the height 
    height = (endpoint - startingpoint) / n
    #The simpson formula is defined as [height/3]  * (  f(x0) + 2*f(x1) + 4(fx2) + 2(fx3)....f(xn)) that is why we need to define the numbers before multiply by 3
    number2 = 2
    number4 = 4
    
    #Prepare to do the summation and since python does 0 based indexing we have  to add 1 to range
    summation = 0.00
    for x in range(n+1):
        #If its the starting point then we just only need to plug in the starting point 
        if(x  == 0):
            summation += function1(startingpoint)
        #If the end point is reached then we just simply plugged it in 
        elif(x == n):
        
            summation += function1(endpoint)
        #If its odd iteration multiply by  4
        elif(x  % 2 == 1 ):
                summation += number4 * function1(0.00 + x * height)
        #If its even iteration multiply by 2 
        elif(x % 2  == 0):
                summation += number2 * function1(0.00 + x * height)
    #Multiply the summation
    integral = (height/3) * summation
    h = round(integral,9)
    return h
    
        
    
#Performs the  simpson method on the second function. We need to also integrate it  as well
def simpsonmethod2():
     #This will be the number of strips to use 
    n = 4000
    #This will be the interval  from [a,b] since the function is only defined from 0 to sqrt(2)
    endpoint = 1.41421356237
    startingpoint = 0.00
    
    #This will be the height 
    height =(endpoint - startingpoint) / n
    
    #The simpson formula is defined as [height/3]  * (  f(x0) + 2*f(x1) + 4(fx2) + 2(fx3)....f(xn)) that is why we need to define the numbers before multiply by 3
    number2 = 2
    number4 = 4
    
    #Prepare to do the summation and since python does 0 based indexing we have  to add 1 to range
    summation = 0.0
    for x in range(n+1):
        #The first iteration
        if(x  == 0):
            summation += function2(startingpoint)
        #The last iteratio
        elif(x == n):
            summation += function2(endpoint)
        #If x is odd 
        elif(x  % 2 == 1 ):
                summation += number4 * function2(startingpoint + x * height)
        #If X is even 
        elif(x % 2  == 0):
                summation += number2 * function2(startingpoint+x * height)
    integral = (height/3) * (summation)
    h = round(integral,9)
    return h
    
    
    
    



    
if __name__ == '__main__':
     main()