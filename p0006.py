# 
# date 05/06/17
# @author Mark Rogan
# 


def squareOfSum(startNum, endNum):
  sum = 0
  for i in range(startNum, endNum):
    sum += i 
  return sum**2

def sumOfSquares(startNum, endNum):
  sum = 0
  for i in range(startNum, endNum):
    sum += i**2
  return sum

if __name__ == "__main__":
  startNum = 1
  endNum = 101
  print (squareOfSum(startNum, endNum)-sumOfSquares(startNum, endNum))
  # print(squareOfSum(startNum, endNum))
  # print(sumOfSquares(startNum, endNum))