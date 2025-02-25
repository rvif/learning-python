from functools import lru_cache 

@lru_cache(maxsize = 1000)
def recursive_fibonacci(n):
    if(type(n) != int):
        raise TypeError("n should be of integer datatype")
    if(n <= 0):
        raise ValueError("n should be a positive number")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)  

for i in range(1, 50): 
    print(i, ":", recursive_fibonacci(i)) 
    