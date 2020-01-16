

#Finds the unique triplets of 3 numbers
#Runs in n^2 + nlogn + n 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
             return []
        if all(v == 0 for v in nums):
            return [[0,0,0]]
        dictionary = {}
        for x in range(len(nums)):
            dictionary[nums[x]] = x
        currentlist = []
        for j in range(len(nums)):
            for h in  range(len(nums)):
                if j != h:
                    if nums[j] + nums[h] != 0:
                        first =   [nums[j],nums[h]]
                        totalsum =sum(first)
                        complement  = 0 - totalsum
                        if complement in dictionary and dictionary[complement] != j and dictionary[complement] != h:
                            newlist = [nums[j],nums[h],complement]
                            newlist.sort()
                            if(newlist not in currentlist):
                                currentlist.append(newlist)
                    elif  nums[j] == 0 and nums[h] == 0:
                        first =   [nums[j],nums[h]]
                        totalsum =sum(first)
                        complement  = 0 - totalsum
                        if complement in dictionary and dictionary[complement] != j and dictionary[complement] != h:
                            newlist = [nums[j],nums[h],complement]
                            newlist.sort()
                            if(newlist not in currentlist):
                                currentlist.append(newlist)
        return currentlist
