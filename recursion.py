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
