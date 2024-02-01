# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseListItr(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head

        while curr_node != None:
            next_node = curr_node.next  # store pointer in temp variable
            curr_node.next = prev_node  # assign prev node to pointer
            prev_node = curr_node       # move prev node to next
            curr_node = next_node       # move curr node to next
        return prev_node

    # Need to go through this method again!
    def reverseListRecursive(self, head: ListNode) -> ListNode:

        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead
        

#Testrun
        
# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result

# Test the reverseListItr method
if __name__ == "__main__":
    solution = Solution()

    # Create a sample linked list
    original_list = [1, 2, 3, 4, 5]
    linked_list = list_to_linked_list(original_list)

    # Print the original linked list
    print("Original Linked List:", original_list)

    # Reverse the linked list using the reverseListItr method
    reversed_head = solution.reverseListItr(linked_list)

    # Convert the reversed linked list to a list and print it
    reversed_list = linked_list_to_list(reversed_head)
    print("Reversed Linked List:", reversed_list)