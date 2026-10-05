#Task 1
#Stack implementation
class Stack:
    def __init__(self):
        self.stack = []

    #Add element to stack
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    #Remove element from stack
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            item = self.stack.pop()
            print(item, "popped from stack")

    #Show top element
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[-1])

    #Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", self.stack)
            #print(self.stack[::-1])

s = Stack()
#Passing values to enter in stack
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
#Displaying stack
s.display()
#Displaying peek element
s.peek()
#Popping top element
s.pop()
#Displaying after poping
s.display()
#Popping top element
s.pop()
#Displaing after poping
s.display()

#Task 2
#Queue implementation
class Queue:
    def __init__(self):
        self.queue = []

    #Add element to queue
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    #Remove element from queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            item = self.queue.pop(0)
            print(item, "removed from queue")

    #Show front element
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element is:", self.queue[0])

    #Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

q = Queue()
#Passing values to enter in queue
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
#Diplaying queue 
q.display()
#Diplaying front element
q.peek()
#Dequeueing top element
q.dequeue()
#Displaying queue after dequeueing
q.display()
#Dequeueing another element
q.dequeue()
#Displaying another element
q.display()

#Task 3
# Binary Search 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# Sorted array
arr = [10, 20, 30, 40, 50, 60, 70]

target = 40

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
