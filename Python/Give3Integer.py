# Given a list of integers, find the highest product you can get from three of the integers. 
# Bruteforce

# define my array
_ints = [13, 2, 8, 4, 9, 3, 11, 2, 7]

list_of_Max_ints = []

def _list_of_Max_ints(list):
   for y in range(len(list)):
      for x in list:
         if (x in list_of_Max_ints) or (len(list_of_Max_ints) == 3):
            for z in list_of_Max_ints:
               if (x > z) and (x not in list_of_Max_ints):
                  list_of_Max_ints.remove(z)
                  list_of_Max_ints.append(x)                                           
         else:
            list_of_Max_ints.append(x)          
   return list_of_Max_ints[0] * list_of_Max_ints[1] * list_of_Max_ints[2]


print(_list_of_Max_ints(_ints))













