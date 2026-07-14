class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        if len(arr) > 1:
            for i in range(len(arr)):
                if arr[i-1] == arr[i]:
                    return True
        return False