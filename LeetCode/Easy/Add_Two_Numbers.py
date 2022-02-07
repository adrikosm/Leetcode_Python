""" 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
    Ex.
        l1 = [2,4,3]
        l2 = [5,6,4]
        342 + 4655 = 807
        so the output is: [7,0,8]
""" 

def add_two_numbers(l1,l2):
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # Get new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10 
        cur.next = ListNode(val)

        # Update pointers
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

def main():
    print(add_two_numbers([2,4,3], [5,6,4]))
    print(add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]))



if __name__ == "__main__":
    main()