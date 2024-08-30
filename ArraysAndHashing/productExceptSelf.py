#Time complexity of O(n), Space Complexity of O(1) (output list does not count towards space complexity)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums)) #initialize a list of 1's of length nums

        pre = 1
        for i in range (len(nums)): #calculate the prefix of each number and store it in the result list
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range (len(nums) - 1, -1 , -1): #calculate the postfix of each number and multiply each prefix by its corresponding postfix
            res[i] *= post
            post *= nums[i]
        
        return res #return the result list
