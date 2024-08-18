#Time complexity O(n), no nested for loops, Space complexity O(n), storing all elements in a hash table
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash = {} #initialize hash table

        for i in range (len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i], 0) #iterate through the list noting every occurence of each number

        for j in range (len(nums)): #check if each number occured more then once
            if hash[nums[j]] > 1:
                return True
        
        return False

        

