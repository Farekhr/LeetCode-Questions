#Time complexity O(m*n) where m is the total number of input strings given and n is the average length of a string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list) #initialize hashmap

        for s in strs: #iterate through each string in the list of strings
            count = [0] * 26 #initialize a count of each letter in a given string

            for c in s: #iterate through each character in a given string
                count [ord(c) - ord("a")] += 1 #count how many times each character appears
            groups[tuple(count)].append(s) #group all strings with a particular character count together
        return groups.values()

 

        



                


        
