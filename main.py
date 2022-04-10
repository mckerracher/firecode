from ListNode import ListNode


class Solution:
    def fibonacci(self, n: int) -> int:
        """
        Returns the nth (zero-indexed) Fibonacci number in the Fibonacci
        sequence 0, 1, 1, 2, 3, 5, 6, ... where n < 15
        :param n: Zero indexed Fibonacci number to return
        :return: Nth Fibonacci number
        """
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def delete_tail(self, head: ListNode) -> ListNode or None:
        """
        Deletes the tail node of the provided linked list.
        :param head: Head node of the singly linked list.
        :return: Head node of the modified list.
        """
        if head is None:
            return None
        elif head.next is None:
            return None
        else:
            temp = head
            while temp.next is not None:
                if temp.next.next is not None:
                    temp = temp.next
                else:
                    temp.next = None

            return head

    def insert_at_front(self, head: ListNode, n: int) -> ListNode:
        """
        Inserts a new ListNode with data n to the front of the singly linked list,
        given the head of the list.
        :param head: Head of the singly linked list.
        :param n: Integer to set on the data property of the inserted node.
        :return: Head ListNode of the modified linked list
        """
        new_head = ListNode(n)
        new_head.next = head
        head = new_head
        return head


if __name__ == '__main__':
    # test solutions here
    sol = Solution

