class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:    # Return true if the list contains duplicates
        # Define a hash set to hold our unique values
        present = set() 
        
        # Iterate through all elements in nums
        for i in nums:
            if i in present:
                return True
            else:
                present.add(i)
        return False