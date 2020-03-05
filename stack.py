# Troy Jeffrey Amegashie
# Stack
# 03/05/2020

from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.mystack = []

    def push(self,data):
        self.mystack.append(data)

    def pop(self):
        return self.mystack.pop()


myList = Stack()
myList.push(3)
myList.push(5)
myList.push(10)
print(myList.pop())
print(myList.pop())
