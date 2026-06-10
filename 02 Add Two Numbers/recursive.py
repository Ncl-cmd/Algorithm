# Definition for a singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
        if not l1 and not l2 and carry == 0:
            return None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        digit = total_sum % 10
        result_node = ListNode(digit)
        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        result_node.next = self.add_two_numbers(next_l1, next_l2, carry)
        return result_node

def to_linked_list(arr: list) -> ListNode:
    """Converts a Python array to a linked list."""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_list(node: ListNode) -> list:
    """Converts a linked list back to a Python array for visualization."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    s = Solution()
    la = to_linked_list([2, 4, 3])
    lb = to_linked_list([5, 6, 4])
    result = s.add_two_numbers(la, lb)
    print(f"Example 1 Output: {to_list(result)}")  # Expected: [7, 0, 8]

    # Test Example 2 (Different sizes)
    l1 = to_linked_list([9, 9])
    l2 = to_linked_list([1])
    output = s.add_two_numbers(l1, l2)
    print(f"Example 2 Output: {to_list(output)}")  # Expected: [0, 0, 1]

    # Test Example 3 (Zero values)
    l1 = to_linked_list([0])
    l2 = to_linked_list([0])
    output = s.add_two_numbers(l1, l2)
    print(f"Example 3 Output: {to_list(output)}")  # Expected: [0]

    # Test Example 4 (Continuous carries)
    l1 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = to_linked_list([9, 9, 9, 9])
    output = s.add_two_numbers(l1, l2)
    print(f"Example 4 Output: {to_list(output)}")  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
