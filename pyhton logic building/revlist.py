def reverse_seq(n):
    a = list(range(1,n+1)) #this creats a arry  for 1 to n+1
    
    return  a[::-1]
   # return list(range(n,0,-1)) does the same thing 

# Example usage:
print(reverse_seq(5))  
