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
