# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:12:55 2018

@author: Wizzhang
"""
import math
import numpy as np
def main():
    array = []
    newarray = [] 
    filename = input("What is your file name: ")
    with open(filename,'r') as f:
        for line in f:
            array.append(line)
    
    for x in range(0, len(array)):
        if "\n" in array[x]:
            cleanedatafield = array[x].replace("\n", "")
            field = cleanedatafield.split("\t")
            datafield = tuple(field)
            newarray.append(datafield)
        else :
            field = array[x].split("\t")
            datafield = tuple(field)
            newarray.append(datafield)
    

  # to see if we are going to use this   
    
    
    for  element  in   newarray:
        #Extract information that is necessary
        
        IR = float(element[0])
        TimetoMaturity = float(element[1])
        numberofpayments = float (element[2])
        volatility = float(element[3]) 
        stockprice = float(element[4])
        strikeprice = float(element[5])
        deltaT = TimetoMaturity /  numberofpayments
        Uscalar = math.exp(volatility * math.sqrt(deltaT))
        Vscalar = 1/Uscalar

        a = math.exp(IR * deltaT)
        numerator = a -Vscalar 
        denominator = Uscalar - Vscalar
     
        p = numerator / denominator
        invp = 1-p
        rows = int(numberofpayments) + 1
        roundedint = int(numberofpayments)
        columns = int(numberofpayments) + 1
        binomialmodel = np.zeros((rows,columns))
        optionmodel = np.zeros((rows,columns))
        binomialmodel[0,0] = stockprice 
        for x in range(1,rows):
            binomialmodel[x,0] = binomialmodel[x-1,0] * Uscalar 
            for j in range(1, columns):
                 binomialmodel[x,j] = binomialmodel[x-1,j-1] * Vscalar 
                 
        for j in range(rows):
            optionmodel[roundedint,j] = max(strikeprice - binomialmodel[roundedint,j], 0 )
            
        for m in range(roundedint):
            i = roundedint - m -1
            for j in range(i + 1):
                optionmodel[i,j] = (p * optionmodel[i+1 , j ] + invp * optionmodel[i + 1,j+1 ]) * math.exp(-IR * deltaT)
                optionmodel[i,j] = max(optionmodel[i,j] ,strikeprice -  binomialmodel[i,j])
        print(str(element) + "The optionvalue is " + str(optionmodel[0,0]))  
        
        
                
if __name__ == "__main__":
    main()