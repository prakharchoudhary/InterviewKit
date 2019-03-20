"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    slow_head = head
    fast_head = head
    while slow_head.next and fast_head.next.next:
        slow_head = slow_head.next
        fast_head = fast_head.next.next
        if slow_head == fast_head:
            return True
    return False
