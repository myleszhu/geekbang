#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# import re
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 先把标点都去除,改为小写
        # onlycharnumS = ''.join(re.findall(r'[A-Za-z0-9]', s)).lower()
        s = ''.join(filter(str.isalnum, s)).lower()
        # print(onlycharnumS)
        # print(len(onlycharnumS))
        # n < len(s)/2, s[n] = s[len(s) - n + 1] , 
        # if <>, return False, else return True
        
        # for i in range(0,len(onlycharnumS)//2):
        #     if onlycharnumS[i] != onlycharnumS[len(onlycharnumS) - i - 1]:
        #         return False
        return s == s[::-1]


        # 

        # # @lc code=end
