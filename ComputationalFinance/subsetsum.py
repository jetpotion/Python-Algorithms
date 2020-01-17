def subsetsum(array:[int],n:int,total:int) -> bool:
    #I know subset sum if very confusing. Dont get me dynamic programming is very poorly taught in computer science education because we take specific instances of problems  and try to shove it down te curriclum
    #Rather dynamic programming is a huge aspect of operation research espeically tabulation.
    table =([[False for i in range(sum+1)]  
            for i in range(n+1)]) 
    #Set the first column to be true because any sum that is zero 
    for i in range(n+1):
        table[i][0] = True
        
    #set the first row to false.
    #  Except the sum that equals == array[0]. Beause we can certainly create a sum with only that element. If we can only pick 1 element
    
    #Let f_i(s) be a recurrence relation to denote the element subset with remainin sum(s)
    #let a say a very simple example s = {1,2,3} and target = 5
    #f_i(s) is f_1(0) f_1(1),f_1(2) , f_1(3),f_1(4), f_1(5)
    #f_2(0).....f_2(5)
    #f_3(0).....f_3(5)
    #As you can seee f_1(0),f_2(0),f_3(0) are all True because we have achieved our ojective based on some set
    #Now we will begin
    #f_3(5) = false because we cannot createa sum with size 1 with 5
    #f_3(4) = false because we cannot create a sum with with just 1 element
    #f_3(3) = True  because we cann create a sum with 3
    #f_3(2) = false ebecause we  cannot create a sum with 2
    #f_3(1) = false  because we cannot create a  sum with just 1
    #f_3(0) = True because our decision is with just 0. And we achieves our object
    #What about length 2?
    #f_2(5)  but this time you will have to think what he  will be deciding from just the elements of size 3. His decision based on f_3(3),f_3(0). Basically choose True
    #f_2(4) He will choose between f_3(4) or f_3(2) basically false
    #f_2(3) he will choose between f_3(3) or f_3(1) basically True
    #f_2(2) he will choose between f_3(0) or f_3(2) which is false 
    #f_2(1) = cant select the current one because he has 1 left. This person is decision is f_3(1) because he cant go further. So its false
    #f_2(0) = true because we have reached object
    #What aobut length(3)? Same process.. on the memmoization. We couldve started at the end of the array or the beginning and weill have  the same answer. With the same decisions



    #Basically this memoization implies an algorithm.
    #  We can either choose to  exclude the current element or not. Carrying over the sum on previous index.
    # # Our decision is binary is based on decision if we take the current index or not

    #loop through everything except for the first  array
    for x in range(len(1,n+1)):
        for j in range(len(1,total+1)):
            if array[x -1 ] > j:
                #This would mean from our current at the currentindex
                #subset then we will be screwed if our sum is zero 
                array[x][j] = array[x-1][j]
            #This case occurs if current sum remaining is greater or equal to the element provided at the current index
            else:
                #The first part of our statement  say that we can choose to exclude the current current index. And our decision was based on the previous step
                #Or we can choose to include it based on the decision 
                array[x][j] = array[x-1][j] or T[i-1][j-array[i-1]
    
    for z in range(len(0,n)):
        for j in len(0,total):
            print(array[z][j], end = " ")
        print("\n")
    return table[n][total]
arr = [1,2,3]
total  =5
length = len(arr)
subsetsum(arr,total,length)
