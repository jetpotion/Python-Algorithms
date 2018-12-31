# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:57:39 2018

@author: wizzhang
"""
import math

def sumprices(pastprices) :
    counter = 0 
    for x in pastprices:
        counter += x
    return counter
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

    
    
    for  element  in   newarray:
        
        #Extract information that is necessary 
        IR = float(element[0])
        
        TimetoMaturity = float(element[1])
        numberofpayments = float (element[2])
        volatility = float(element[3]) 
        stockprice = float(element[4])
        strikeprice = float(element[5])
        deltaT =  TimetoMaturity / numberofpayments
        Uscalar = math.exp(volatility * math.sqrt(deltaT))
        Vscalar  = 1/Uscalar
        p = (math.exp(IR  * deltaT) - Vscalar) / (Uscalar - Vscalar) 
       
        invp = 1-p
        binomialmodel = [] 
        for x in range(0, 2 **(int(numberofpayments)+1) - 1):
            binomialmodel.append(-1)
        
        
        binomialmodel[0] = (stockprice,stockprice,1)
        
        for x in range(1,len(binomialmodel)):
            parentindex = (x-1)//2
            leftchild =  2 * parentindex + 1
            rightchild = 2 * parentindex + 2
            parent = binomialmodel[parentindex]
          
            newtime = parent[2] + 1  
            Upwardprice = parent[0] * Uscalar
            Downwardprice = parent[0] * Vscalar 
            average = parent[1]     
            newupwardaverageprice = (parent[2] * average + Upwardprice) / newtime 
            newdownwardaverageprice = (parent[2] * average  + Downwardprice) / newtime                      
            binomialmodel[leftchild ] = (Upwardprice,newupwardaverageprice, newtime)
            binomialmodel[rightchild] = (Downwardprice,newdownwardaverageprice,newtime )
            
            
            
       
    #    print(binomialmodel)
        for b in range(0, len(binomialmodel)):
            extractedelement = binomialmodel[b]
            binomialmodel[b] = max(extractedelement[1] - strikeprice , 0 )
      
        
        for x in range(len(binomialmodel)-1,0,-1):
            parent = (x-1) //2
            leftchild = 2 * parent + 1
            rightchild = 2 * parent + 2
            binomialmodel[parent] = (p * binomialmodel[leftchild] + (invp * binomialmodel[rightchild])) * math.exp(-IR * deltaT)
            
        
        print(str(element) + " The binomialprice of the asian option is " + str(binomialmodel[0]))
     

       
        
        
if __name__ == "__main__":
    main()
