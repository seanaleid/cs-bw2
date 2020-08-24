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
import re

# s='Hi! some stuff * &, xyz'
# print(re.sub(r'\W', '',s))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]', "", s).lower()
        s2 = s[::-1]

        return s == s2

