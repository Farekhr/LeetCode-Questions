#Time complexity O(n) and space complexity O(n) due to the dictionary used
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} #initialize dictionary to store the numbers as the key and their counts as the value

        freq = [[] for i in range(len(nums) + 1)] #initialize frequency list to store each number as theindex and its count as the value

        for j in nums:
            count[j] = 1 + count.get(j, 0) #add all numbers and thier counts into the dictionary

        for n,c in count.items():
            freq[c].append(n) #append each frequency n to the list and have c (the index) be its actual value

        result = [] #initialize the return list

        for i in range (len(freq) - 1, 0, -1): #iterate through the frequency list from most to least
            for n in freq[i]: 
                result.append(n) #since freq[i] could be a lit in itself, append all its items to result
                if (len(result) == k): #when result's length is k, return the result list
                    return result
