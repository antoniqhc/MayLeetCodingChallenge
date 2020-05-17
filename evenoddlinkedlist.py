# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # edge case
        if head == None:
            return head
        
        # init all variables
        n = 0
        num_odds = 0
        count = head
        odd_head = head
        even_head = head.next
        parse_head = head
        while count != None:
            n += 1
            count = count.next

        num_odds = n//2
        if n%2 == 1:
            num_odds += 1
        num_evens = n - num_odds
        
        # handle odds first
        i = 1
        while i <= num_odds:
            jump_ahead = (i*2)-1
            copy = odd_head
            for j in range(jump_ahead-i):
                copy = copy.next

            append_val = odd_head.val
            if type(append_val) == str:
                append_val = int(append_val.split(' ')[0])
                
            odd_head.val = str(append_val) + ' ' + str(copy.val)
            i += 1
            odd_head = odd_head.next
            
        # now handle evens
        i = 2
        while even_head != None:
            if i%2 == 0:
                jump_ahead = num_odds + (i//2)
                alter = even_head
                for j in range(jump_ahead-i):
                    alter = alter.next
                append_val = even_head.val
                if type(append_val) == str:
                    append_val = int(append_val.split(' ')[0])

                alter.val = str(alter.val) + ' ' + str(append_val)

            i += 1
            even_head = even_head.next
            
        while parse_head != None:
            parse_head.val = parse_head.val.split(' ')[1]
            parse_head = parse_head.next
                
        return head