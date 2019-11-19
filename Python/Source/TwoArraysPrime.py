# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
# 51 R = 0
# 50

#100 99 98 97 96 95 94 93 92 91 R = 0
#1 2 3 4 5 6 7 8 9 10

def divE(x, Array):  
  for i in Array:
     if (x%i != 0):
       return False
  return True    
    
def divD(x, Array):  
  for i in Array:
     if (i%x != 0):
       return False
  return True

def getTotalX(a, b):
    r = []    
    for i in a:
        x = [0]                        
        while x >= (a[len(a) - 1]):           
          if divE(x,a) and (not r.__contains__(x)):  
            r.append(x)
          x -= 1  
    p = []      
    for h in r:
      if divD(h, b):
        p.append(h)
    return len(p)    

  


#a = [2, 4]
#b = [16, 32, 96]

a = [51]
b = [50]
resp = getTotalX(a, b)  

print(resp)