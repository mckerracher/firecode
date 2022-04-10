class ListNode:
    """
    This class represents a node of a singly linked list. The `data` field holds
    the data value of this node, and the `next` field holds a reference to the
    next node in the linked list, which is `None` if this is the last node in the list.
    """

    def __init__(self, data: int, next: 'ListNode' = None):
        self.data = data
        self.next = next  # None by default
