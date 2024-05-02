# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        def mergeKLists(self, lists: List[[ListNode]]) -> ListNode:
            if not lists or len(lists) == 0:
                return None
            
            while len(lists) > 1:
                mergedLists = []

                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    list2 = lists[i + 1] if (i + 1) < len(lists) else None
                    mergedLists.append(self.mergeTwoLists(list1, list2))
                lists = mergedLists #why
            return lists[0] #why


        def mergeTwoLists(self, list1, list2):
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next

                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2
            

            return dummy.next




    


#######################################
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
    List1 = [1, 2, 3, 4, 5]
    llist1 = list_to_linked_list(List1)

    # Print the original linked list
    print("Original Linked List:", List1)

    # Create a sample linked list
    List2 = [3, 4, 8, 9]
    llist2 = list_to_linked_list(List2)

    # Print the original linked list
    print("Original Linked List:", List2)


    # Reverse the linked list using the reverseListItr method
    mergelist = solution.MergeList(llist1, llist2)

    # Convert the reversed linked list to a list and print it
    merged_list = linked_list_to_list(mergelist)
    print("Merged Linked List:", merged_list)