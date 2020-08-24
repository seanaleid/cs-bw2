# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases. 

# Note: For the purpose of this problem, we define empty strings as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: True

# Example 2:
# Input: "race a car "
# Output: False

# Example 3:
# Input: "racecar"
# Output: True

# Source: https://leetcode.com/problems/valid-palindrome/submissions/
from re import sub

# s='Hi! some stuff * &, xyz'
# print(re.sub(r'\W', '',s))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ OPTION 5 """
        # recursive solution
        # s is a palindrome if:
        #     s is len 0 or 1 (BASE CASE)
        # or
        #     the first and last characters are the same
        #     and if the substring between the first and last chracters is a palindrome
        
        # driving a recursive solution towards a basecase, example:
        # def loop(n):
        #     if n == 0:
        #         return
        #     loop(n-1)
        # loop(5)

        s = "".join(c for c in s if c.isalnum()).lower()
        
        def ispal(s):
            if len(s) < 2:
                return True
            return s[0] == s[-1] and ispal(s[1:-1])
        return ispal(s)

        """ OPTION 4 """
        #     if s == "":
        #     return True
        
        # i0 = 0
        # i1 = len(s)-1
        
        # while i1 > i0:
        #     if not s[i0].isalnum():
        #         i0+=1
        #         continue
        #     if not s[i1].isalnum():
        #         i1-=1
        #         continue
        #     if s[i0].lower() != s[i1].lower():
        #         return False
            
        #     i0+=1
        #     i1-=1
            
        #     return True


        """ OPTION 3 """
        # s = "".join(c for c in s if c.isalnum()).lower()
        
        # i0 = 0
        # i1 = len(s)-1
        
        # while i1 > i0:
        #     if s[i0] != s[i1]:
        #         return False
            
        #     i0+=1
        #     i1-=1
        # return True
        
        """ OPTION 2 """
        # s = sub(r'[\W_]', "", s).lower()
        # # s = "".join(c for c in s if c.isalnum()).lower()
        
        # i0 = 0
        # i1 = len(s)-1
        
        # while i1 > i0:
        #     if s[i0] != s[i1]:
        #         return False
            
        #     i0+=1
        #     i1-=1
        # return True

        """ OPTION 1 """
        # s = re.sub(r'[\W_]', "", s).lower()
        # s2 = s[::-1]

        # return s == s2
        
