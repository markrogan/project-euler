# 
# date 01/06/17
# @author Mark Rogan
# 


def checkProduct(x,y):
  product = x*y
  product = str(product)
  reverse = product[::-1]
  if (product == reverse) :
    return int(product)
  else :
    return 0

def getLargestPalindrome(startNum, endNum):
  largest = 0
  for i in range(startNum, endNum) :
    for j in range(startNum, endNum) :
      current = checkProduct(i, j)
      if(current > largest) :
        largest = current
  return largest


if __name__ == "__main__":
  print(getLargestPalindrome(100,999))