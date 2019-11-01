#To do this, you’ll need to know when any team is having a meeting. 
# In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
# These integers represent the number of 30-minute blocks past 9:00am. 

array_tuplas = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]



def merge_tuple(_tuple1, _tuple2):
   List_01 = range(_tuple1)
   List_02 = range(_tuple2)

   for x in List_01:
      if x in List_02:
           List_02.remove(x)

   for x in List_02:
      if x in List_01:
           List_01.remove(x) 

Arr = []

for z in len(array_tuplas):
   if z > 0:
    Arr        
