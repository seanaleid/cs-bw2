# Source: https://leetcode.com/problems/add-two-numbers/
# Resource: https://www.youtube.com/watch?v=SbcCpAw_8Dg
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# U --> return a singly linked list as the sum of the two other linked lists in reversed order
# P --> take LL and reverse, join, make int, sum, take sum, split, reverse and return
# E
# R


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # """ PROPER SOLUTION, WORKS ON LEET CODE """
        # carry value to leap frog in reverse order and carry adding l1.val + l2.val if greater than 10
        # currentCarry = 0
        # declare cur variable to help traverse and add nodes to new list. declare head variable to be the head of the list
        # head = cur = ListNode(0)
        
        # iterate using a while loop
        # while l1 or l2 or currentCarry:
            # determine the current value and the carry value
            # currentVal = currentCarry
            # currentVal += 0 if l1 is None else l1.val
            # currentVal += 0 if l2 is None else l2.val
            
            # if currentVal >= 10:
            #     currentVal-=10
            #     currentCarry = 1
            # else:
            #     currentCarry = 0
            
            # add current value as it will always be at least '1'
            # cur.next = ListNode(currentVal)
            # cur = cur.next
            
            # add base case for iterating linked lists
            # if l1 is None and l2 is None:
            #     break
            # elif l1 is None:
            #     l2 = l2.next
            # elif l2 is None:
            #     l1 = l1.next
            # else:
            #     l1 = l1.next
            #     l2 = l2.next
        # return next node
        # return head.next
        
        # """ FIRST PASS, doesn't pass leet code, but gives the correct answer """
        # newL1 = ""
        # for n in l1[::-1]:
        #     newL1+=str(n)
        
        # newL2 = ""
        # for n in l2[::-1]:
        #     newL2+=str(n)
        
        # result = int(newL1) + int(newL2)
        # newResult = [int(i) for i in str(result)]
        
        # return newResult[::-1]

# s = Solution()
# print(s.addTwoNumbers([2,4,3], [5,6,4]))

# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         greatest = max(candies)
#         for n in candies:
#             if n + extraCandies >= greatest:
#                 return True
#             else:
#                 return False

def kidsWithCandies(candies, extraCandies):
    greatest = max(candies)
    for i, n in enumerate(candies):
        # print(i, n)
        if n+extraCandies >= greatest:
            candies[i] = True
        else:
            candies[i] = False
    return candies

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))