#A particularly hard problem to solve
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     #Get the lenghts of the two arrays
        x = len(nums1)
        y = len(nums2)
    #Since we always want the median of the smaller array. We will want to swap them. If they are equal then this doesnt matter
    #Since python is extremely anal about calling methods on itself in a clas. We have to say self
        if y  < x:
             return self.findMedianSortedArrays(nums2,nums1)
        start = 0
        end = x
    #If start becomes greater than the end then we cant partitition arrays  in ascending order
        while(start <= end):
            #Create a partition based on the (start + (min(x,y))/2)
            pivotx = int((start + end)/2)
            pivoty = int((x + y + 1)/2) - pivotx
            #These cases occur if find that a partition is the length of the entire array 
            #Particularly the mininums edge case occurs if the pivot winds up taking up the arrya
            #The maximum edge cases occurs if the pivot gets completely reduced to zero
            maxLeftX = -(sys.maxsize-1 ) if pivotx == 0  else nums1[pivotx-1]
            minRightX = sys.maxsize if pivotx ==  x else nums1[pivotx]
            maxLeftY = -(sys.maxsize-1) if pivoty ==  0 else nums2[pivoty-1]
            minRightY = sys.maxsize if pivoty ==  y else nums2[pivoty]
            #We care about these specific integers to get the conclusion we so desired. 
            #Which is the maximum of the Left partitions of each array and the minimum of each partition in the Right partition of each arryas
            #It is up the reader to understand why we can get the medium through these four numbers
            if(maxLeftX <= minRightY and maxLeftY <= minRightX):
            #We found the correct partition 
            #return their specific cases
                    #In the case of even. The median the average of the maximum(maxLeftx,maxLefty) and min(minRightX,minRightY)
                    if (x+y) % 2 == 0:
                        maximum = max(maxLeftX,maxLeftY)
                        minimum = min(minRightX,minRightY)
                        return float((maximum + minimum)/2 )
                    #Otherwise its the maximum between the maximum of the left partition of X and Y
                    else:
                        return float(max(maxLeftX,maxLeftY))
             #We gone too far in the array. We need to move the pivot back
            elif maxLeftX > minRightY:
                end = pivotx -1
            else:
            #We gone too far back in the array. We need to the move the pivote forward
                start = pivotx + 1    
