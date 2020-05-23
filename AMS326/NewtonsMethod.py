# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:24:14 2019

@author: William Zhang
#ID : 110768508
@email: William.Zhang@stonybrook.edu
"""

import numpy as np 
import matplotlib.pyplot as plt
"The main method as a driver to plot the graph "
def main():
    plotting = np.arange(-1,2,0.001)
    plt.plot(plotting,function(plotting))
    
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("A function of X")
    plt.grid(True)
    bisectionMethod()
    plt.show()
    
"This is the function "
def function(x):
    h = -np.power(x,3)
    sinfunction = np.power(x,4)
    return np.power(2.019,h) - np.power(x,5) * np.sin(sinfunction) - 1.984
"This method to make sure these intervals are opposite signs "
def sameSign(a,b):
    return a * b > 0;
"Now we apply the bisection method "
def  bisectionMethod():
    #This are our boundary we think are on the graph are between [-1,2] #
    #Our X1 were = [-0.8,1.35,1.55,1.75,1.95]
    x1 = [-0.8,1.35,1.55,1.75,1.95 ]
    
    #These were my intervals and we are going to use. My program will also print the error  as well the root.
    intervals = [[-0.7,-0.9],[1.3,1.4],[1.5,1.6],[1.7,1.8],[1.9,2.0]]
    
    "Maximum number of iterations. Of course there are more optimal ways to determine this number"
    "but a  1000 iterations  can give us a number potentially  accurate to thousands place.The more iterations the more accurate the root is"
    iterations = 1000
    for x in range(0,5):
        #left boundary  interval 
        a = intervals[x][0]
        #Right boundary interval
        b = intervals[x][1]
        #Check to make sure they are not the same sign 
        assert not sameSign(function(a),function(b))
        
        for h in range(iterations):
            c = (a + b)/2
            #Check if the function is zero
            if(round(function(c),4) is 0.00000 ):
                error =  round(abs(x1[x]) -abs(intervals[x][0]),4)
                print("Boundaries: " + str(intervals[x]) + "\tRootX1: " + str(x1[x]) + "\tError: " + str(error) + "\tRootx0: " + str(c))
            #Check if they are the same sign 
            elif(sameSign(function(a), function(c))):
                a = c
            else: 
                b = c
        error = round(abs(x1[x]) -abs(intervals[x][0]),4)
        print("Boundaries: " + str(intervals[x]) + "\tRootx1: " + str(x1[x]) + "\tError: " + str(error) + "\tRootx0: " + str(c))
    
    
    
    
    
    
    
    
if __name__ is "__main__":
    main()