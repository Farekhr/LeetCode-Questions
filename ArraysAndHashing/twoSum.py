class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Sums = {} #initialize dictionary to store all previously visited elements in the list

        for n in range(len(nums)): #iterate through the list
            complement = target - nums[n] 
            if complement in Sums: #check to see if the complement of our number to the target value exists in the dictionary
                return[Sums[complement], n] #return the indeces of the complement as well as the index of the current value

            
            Sums[nums[n]] = n #add the current value of the number in the list as the key, and its index as the value to be able to later access its index when needed
