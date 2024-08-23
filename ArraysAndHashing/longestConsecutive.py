#Time Complexity O(n) because of the single for loop. Space complexity O(n) because of the hashset
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers = set(nums) #initialize hashset to store all elements in nums
        longest = 0

        for i in nums: #iterate through all elements in nums
            if (i - 1 not in numbers): #check if a number is the start of a sequence by seeing if the number - 1 exists in the hashset
                length = 0
                while(i + length in numbers): #keep adding 1 to the length while a number  + 1 still exists in the hashset
                    length += 1
                longest = max(longest, length) #determine if it is the longest sequence so far
        return longest #return the longest sequence

