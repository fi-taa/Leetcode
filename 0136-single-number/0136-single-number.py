class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        print(hash)
        for i in hash:
            if hash[i] == 1:
                return i
        return -1
        