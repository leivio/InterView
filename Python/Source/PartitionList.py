# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Input: head = 1->4->3->2->5->2, x = 3
# Output:       1->2->2->4->3->5

# define values
_arr = [1, 4, 3, 2, 5, 2]

#Create class
class TreeNode:
  def __init__(self, Value, left=None, rigth=None):
    self.value = Value
    self.left = left     
    self.rigth = rigth  
  def __str__(self):
    return str(self.value)


   




