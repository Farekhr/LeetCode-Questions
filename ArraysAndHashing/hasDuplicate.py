#Time complexity O(n), no nested for loops, Space complexity O(n), storing all elements in a set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashtable = set() #initialize set

        for i in nums: #iterate through the list
            if i in hashtable:
                return True #return true if a number has previously been stored in the set
            hashtable.add(i) #otherwise add the number to the set
        
        return False

        

