# Title: Implement Queue using Stacks
# Source: https://leetcode.com/problems/implement-queue-using-stacks/

# Instructions:
# Implement the following operations of a queue using stacks.
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

# Examples:
# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false

# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. 
# You may simulate a stack by using a list or dequeue (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

class MyQueue:

    def __init__(self):
        self.storage = list()
        self.size = len(self.storage)
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.size+=1
        self.storage.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size == 0:
            print("Sorry, nothing here!")
        else:
            popped = self.storage.pop(0)
            self.size = self.size - 1
            return popped
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.size == 0:
            print("Sorry, nothing here!")
        else:
            peeked = self.storage[0]
            return peeked
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size == 0:
            return True
        else:
            return False
            
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()