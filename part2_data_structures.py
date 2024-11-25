# Array Implementation
class Array:
    def __init__(self, size):
        self.array = [None] * size
    
    def insert(self, index, value):
        self.array[index] = value
    
    def delete(self, index):
        self.array[index] = None
    
    def access(self, index):
        return self.array[index]

# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        return self.stack[-1] if self.stack else None

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

# Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        
        if not temp:
            return
        
        prev.next = temp.next
        temp = None

# Example usage
if __name__ == "__main__":
    arr = Array(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    print(arr.access(1))  # Output: 20
