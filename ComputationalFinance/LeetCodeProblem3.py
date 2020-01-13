#I dont know what leetcode was thinking by adding random cases such  as a space. This is what known as the schedule window procedure on iterative arrays
#Scan through the array
  #If we havent seen it before append to our "window"
  #If we did see it before "destroy" everything before and including the repeated elements 
#Return the final window
#Finds the longest substring without repeated characters
#Runs at most O(n) + O(Rn) amount of work on the array. Where R is the portion of the array that we wanted to slice off.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CLS = ""
        substring = ""
        if s is " " or len(s) == 1:
            return 1
        
        for x in s:
            #Start creating the subsequence
            if x not in substring:
                substring += x
            #If we encounter a character we havent seen before
            else:
                if len(substring) > len(CLS):
                    CLS  = substring
                location = substring.find(x)
                if(len(substring) == 1 or location == (len(substring) -1)):
                    substring = ""+x
                else:
                    substring = substring[location + 1:] + x
          #If nothing was changed          
        if(len(substring) > len(CLS)):
            CLS = substring
            
        return len(CLS)
       
