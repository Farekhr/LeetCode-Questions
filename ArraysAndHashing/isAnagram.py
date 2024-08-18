#Time complexity of O(n), no nested for loops, Space Complexity of O(n), had to use a dictionary to achieve O(n) Time.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #Automatically return false if both strings are not the same length
            return False

        letters = {} #initialize dictionary

        for i in s:
            letters[i] = letters.get(i, 0) + 1 #iterate through the first string and add to the count of each letter in the dictionary

        for j in t:

            if j not in letters: #check is second string has any letters that first string didn't have
                return False
            
            if letters[j] < 1: #check if any letter appears more times in second string then it does in the first
                return False
            
            if j in letters: #subtract one from count to make sure duplicates are treated as seperate letters
                letters[j] = letters.get(j, 0) - 1

        return True 
