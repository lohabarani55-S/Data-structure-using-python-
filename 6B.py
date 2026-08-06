from collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

class PalindromeChecker:
    def is_palindrome(self, text):
        stack = Stack()
        queue = Queue()

      
        for ch in text:
            if ch.isalnum():
                ch = ch.lower()
                stack.push(ch)
                queue.enqueue(ch)
        for i in range(len(stack.items)):
            if stack.items[len(stack.items) - 1 - i] != queue.items[i]:
                return False
