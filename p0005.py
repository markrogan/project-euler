# 
# date 01/06/17
# @author Mark Rogan
# 

def isDivisible(x,y, num):
  divisible = True
  # print num
  # print x + y
  for i in range(x,y):
    if(num % i != 0):
      # print (num % i)
      divisible = False
  return divisible

def findLowest(lowFactor, highFactor):
  found = False
  iteration = 0
  while(found is ):
    iteration+=1
    found = isDivisible(lowFactor, highFactor, (iteration*highFactor))
  if(found is True):
    return iteration*highFactor
  else:
    return "No number found"

if __name__ == "__main__":
  findLowest(1, 20)