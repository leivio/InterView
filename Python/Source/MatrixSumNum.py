'''
Similar as 240. Search a 2D Matrix II, all row and col direction are sorted, find all two sum pairs in matrix such that two sum equal to target.

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

given target=9, return [[1,8],[2,7],[3,6],[4,5]],
order does not matter, [3,6] are same as [6,3],do not include duplicate pair.
my idea is use hashmap, which cost O(m*n) time.
'''

matrix = [
           [1,   4,  7, 11, 15],
           [2,   5,  8, 12, 19],
           [3,   6,  9, 16, 22],
           [10, 13, 14, 17, 24],
           [18, 21, 23, 26, 30]
         ]

_target = 9
dic = {}

def addItem (a, b, target):
  for i in a:
    for j in b:      
      if (i + j == target):
        if (i * j) != dic.keys:
          dic[i * j] =  (i, j)

for i in matrix:
  for j in matrix: # if i != j:
    addItem(i, j, _target)

print(dic)      

    

