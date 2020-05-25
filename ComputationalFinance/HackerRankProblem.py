import math
import os
import random
import re
import sys
#Hacker rank problem Library and roads
# Complete the roadsAndLibraries function below.
#n: integer, the number of cities
#c_lib: integer, the cost to build a library
#c_road: integer, the cost to repair a road
#cities: 2D array of integers where each. Which cities[i] is a element [x1,y1]  to denote a connection between two cities. For which there are M connections

def roadsAndLibraries(c_road,c_lib, n, cities):
    #These are the cities 
    #Decide what our data structure will be 
    
    #A boolean set to get the visited
    visitedset = [False for x in range(0,n)]
    Edgeset = {}
    Visitedcardinality = n
    Connectionsize = 0
    #Will run on #Edges
    for connections in cities:
        sourcevertex = connections[0]
        targetvertex = connections[1]
        #Base case. Our loop will break when have visited on each of the N cities, The thing is were not constructing the graph before we start and were just funneling through edges
        #Runs O(V + E). This is not linear by any means because the #edges could be v(v-1) large but this is okay because our function depends on two variables which is hte edges and vertices
        if(Visitedcardinality  == 0):
            break
        #This means that we have encountered a target we have not sceen before 
        if visitedset[targetvertex-1] == False:
            visitedset[targetvertex-1] == True
            #dfsgraph[sourcevertex-1][targetvertex-1] == True
            Visitedcardinality -= 1
            Connectionsize  += 1
            if(sourcevertex not in Edgeset):
                Edgeset[sourcevertex] = [targetvertex]
            else:
                Edgeset[sourcevertex].append(targetvertex)
            #Condition applies when the above condition is true 
            if visitedset[sourcevertex-1] == False:  
                visitedset[sourcevertex-1] == True
                Visitedcardinality -= 1 
             #   dfsgraph[targetvertex-1][sourcevertex-1] == True
    #We have no choice  the graph that results in this dfs give us J number of disconnected component. However this will  reduce how many operations. We need to do on the graph
    #The order of complexity to
    vertices = Edgeset.keys
    Hasbeenincremented = False
    visitedset = [False for x in range(0,n)]
    connectedcomponent = 0 
    #We are working on a dfs graph
    for vertex in vertices:
            if visitedset[vertex] == False:
                visitedset[vertex] = True
                for edge in  Edgeset[vertex - 1]:
                #This is the way to detecte
                    if visitedset[edge-1] == False:
                        visitedset[edge-1] == True
            elif visitedset[vertex] == True
                for edge in Edgeset[vertex-1]:
                    if visitedset[edge -1] == False:
                        visitedset[edge-1] == True 
                        if Hasbeenincremented == False:
                            connectedcomponent += 1
                            Hasbeenincremented  = True
         #Then do this on every vertex   
        Hasbeenincremented =  False 

#Now were ready to calculate the minimum  between choosing only 1 library per each conected component and has  building all the roads. Or build libraries in every single city
return min(c_road * connectionsize +  connectedComponent *  c_lib, c_lib * N )
