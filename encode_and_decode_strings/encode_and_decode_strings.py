class Solution:
    def encode(self, strs: List[str]) -> str:
        # to hold the resulting string
        res = ""

        for s in strs:
            # for each element in strs, append the number of characters followed by a # delimiter
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        # i will hold our place in the string as we parse through it
        i = 0

        while i < len(s):
            # j is a pointer to parse length of word
            j = i
            
            # move j up until it gets to the delimiter
            while s[j] != "#":
                j += 1
            
            # the length of the word is given by the integer present until #
            length = int(s[i:j])

            # the word can be isolated as a substring, starting at j + 1 (after #) and has length "length"
            res.append(s[j + 1: j + 1 + length])
            
            # shift up pointer i to the start of the next word
            i = j + 1 + length
        
        return res