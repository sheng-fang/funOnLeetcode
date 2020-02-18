"""
Data structure includes several implementations of basic data structure.

1. LinkedList
"""


class Node:
    def __init__(self, val=None, previous_node=None, next_node_l=None, next_node_r=None):
        self.value = val
        self.previous_node = previous_node
        self.next_node_l = next_node_l
        self.next_node_r = next_node_r


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __insert__(self, node: Node):
        assert node is not None

        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.tail.next_node_l = node
            node.previous_node = self.tail
            self.tail = node
            self.length += 1

    def __delete__(self, node: Node):
        assert node is not None
        assert self.length > 0

        node.previous_node.next_node_l = node.next_node_l
        node.next_node_l.previous_node = node.previous_node

        self.length += 1

    def __search__(self, val):
        if self.head is None:
            return -1

        curr_node = self.head
        tar_node = -1
        while curr_node is not None:
            if curr_node.val == val:
                return curr_node
            else:
                continue
