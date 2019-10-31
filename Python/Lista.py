#coding: utf-8

class Node:
  def __init__(self, _Prior, _Val):
    self.valor = _Val
    self._Prior = _Prior     
    if _Val > 1:
      _Prior = self

N = None
for x in range(1, 10):
  N = Node(N, x)  

while not (N._Prior is None):
  print(N.valor) 
  N = N._Prior
  
print(N.valor) 
    