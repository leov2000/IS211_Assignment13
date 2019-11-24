def fibonacci(num):
    if num < 1:
        return num
    
    if num == 1:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)

def gcd(a,b):
    if not b :
        return a
    
    return gcd(b, a % b)
 
def compareTo(s1, s2):
  if(s1 == s2):
    return 0
  elif(s1 > s2):
    return 1
  elif(s1 < s2):
    return -1
  else:
    return compareTo(s1[1:], s2[1:])