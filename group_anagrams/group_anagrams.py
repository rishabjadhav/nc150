class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        # define a defaultdict (doesn't throw error if value in k:v is null)
        # this dict stores words that are anagrams of one another, in lists
        dct = defaultdict(list)

        # iterate through each word in strs
        for w in strs:
            # holds the frequency of each char (a - z) in the word
            wcount = [0] * 26

            # iterate through each character in the word
            for s in w:
                # add one to the element in the list whose index corresponds to the rank of the character (a=0,b=1)
                wcount[ord(s) - ord('a')] += 1

            # add the word to the list of words for which the frequency list of chars matches (hence anagrams)
            # note that we must typecast the freq. list to a tuple, as mutable data types cannot be dict keys
            dct[tuple(wcount)].append(w)

        # values() returns all elements, must be typecasted to list
        return list(dct.values())