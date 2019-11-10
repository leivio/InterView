# Soma de duas listas
#
#
class ListNode(object):
   def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):                       
      c = None
      while (l1 and l2):        
        b = ListNode(l1.val + l2.val)
        b.next = c
        c = b
        l1 = l1.next
        l2 = l2.next
        
      while b:        
        print(b.val)
        b = b.next

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

S = Solution()
S.addTwoNumbers(a1, b1)            