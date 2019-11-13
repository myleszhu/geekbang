#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow = 0
            for fast in (1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0


# @lc code=end

