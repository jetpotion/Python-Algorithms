class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newmap = {}
        for x in range(len(nums)):
            newmap[nums[x]] = x
        for j in range(len(nums)):
            complement = target - nums[j];
            if complement  in  newmap.keys() and newmap[complement] != j:
                return [j,newmap[complement]]
