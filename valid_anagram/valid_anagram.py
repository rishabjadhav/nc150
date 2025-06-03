class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    # Returns true if strings s and t are anagrams of eachother
        # ensure s and t are the same length, they cannot be anagrams if they are not the same length
        if (len(s) != len(t)):
            return False
        
        # create two dictionaries for the key (char) and value (# of occurences) of s and t
        countS = dict()
        countT = dict()

        for i in range(0, len(s)):
            # increment the value (occurences) by one for each char appearance
            countS[s[i]] = 1 + countS.get(s[i]) 
            countT[t[i]] = 1 + countT.get(t[i])

        # compare the dicts like this
        return countS == countT