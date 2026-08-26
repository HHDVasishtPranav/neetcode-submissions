class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp1 = target - nums[i]
            for k in range(i+1,len(nums)):
                if nums[k] == temp1:
                    ans.append(i)
                    ans.append(k)
        return ans