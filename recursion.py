def fibonacci(num):
    if num < 1:
        return num
    
    if num == 1:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)

def gcd(a, b):
    if not b :
        return a
    
    return gcd(b, a % b)
 
def compareTo(s1, s2):
  """
  A recursive function that compares one string to another.

  Parameters:
    s1(string)
    s2(string)

  Returns:
    0 if they equal
    1 if s1 is greater
   -1 if s2 is greater
  """
  if(s1 == s2):
    return 0
  elif(s1 > s2):
    return 1
  elif(s1 < s2):
    return -1
  else:
    return compareTo(s1[1:], s2[1:])