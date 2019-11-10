'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



class Solution(object):
    def twoSum(self, nums, target):            
        arr = []
        for i in range(len(nums)):
            out = target - nums[i]
            if (out in nums) and (nums.index(out) != i):              
              arr.append(nums.index(nums[i]))
        return arr 


class Solution(object):
    def twoSum(self, nums, target):        
        for x in range(0, len(nums)):
            for i in range(0, len(nums)):
                if ((nums[x] + nums[i] == target) and (x <> i)):                    
                    return [x, i]
        
                   
'''
class Solution:
    def twoSum(self, nums, target):
        ouput = 0
        for i in range(len(nums)) :
            output = target - nums[i]
            if (output in nums) and (nums.index(output) != i):
                break
                
        first_indx = i
        second_indx = nums.index(output)
        
        return [first_indx, second_indx]

nums = [3, 4 , 3, 2]  
target = 6
S = Solution
a = S.twoSum(S, nums, target)      
print(a)

