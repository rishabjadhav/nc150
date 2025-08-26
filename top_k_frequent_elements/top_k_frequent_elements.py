class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # holds the # of occurences of each value, key is the element in nums, value is # occurences
        count = {}

        # each list in freq corresponds to all elements in nums that occur as many times as the index of the list
        # the number of lists in freq should be size of nums, as a value in nums can only appear at most len(nums) times
        freq = [[] for i in range(0, len(nums) + 1)]

        for n in nums:
            # increment frequency of n if it appears, defaulting to 0 if unseen
            count[n] = 1 + count.get(n, 0)
        # k is key, v is value, given as key-value pairs in count
        for key, v in count.items():
            # add the key (element in nums that appears v times) to freq, in index v, where v is the frequency of k
            freq[v].append(key)

        # list to hold the returned value of K most frequent elements
        result = []

        # iterate from the last index in freq to 0, decreasing
        for i in range(len(freq) - 1, 0, -1):
            # for each element in a sublist of freq
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

