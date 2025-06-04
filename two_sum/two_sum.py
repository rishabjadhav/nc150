class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict for nums
        nms = {}

        # iterate through all nums
        for i in range(len(nums)):
            # before adding num at index i, check if target - nums[i] is in dict
            if target - nums[i] in nms:
                # this means we've found our complement
                return [i, target - nums[i]]
            
            # key is the number at i, value is the index i
            nms[nums[i]] = i
