# Troy Jeffrey Amegashie
# Linked Lists in Python
# 02/24/2020


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return repr(self)


class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)


class Stack:
    def __init__(self):
        self.mystack = []

    def push(self,data):
        self.mystack.append(data)

    def pop(self):
        return self.mystack.pop()









