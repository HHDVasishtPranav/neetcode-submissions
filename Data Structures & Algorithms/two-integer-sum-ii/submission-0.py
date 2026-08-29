# #mindM the algofor 2-pointer :
# left = 0 
# right = len(num) - 1# since starts with 0
# while left<right:
#     ,,,,
#     move left and right based on the > < = or what ever logic
# return
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:#only works on sorter
            if numbers[l] + numbers[r] < target:
                l = l+1
            elif numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                r = r-1
        return [l,r]