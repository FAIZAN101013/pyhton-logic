numlist = []
for _ in range(5):
    i = input("enter the number: ")
    numlist.append(i) 
numlist.sort()
print(f'The Second largest Number is {numlist[-2]}')   
    
    
def sec_largest(nums):
    F , S = float('-inf') , float('-inf') #-inf negetive infinity
    for num in nums:
        if num > F :
            S = F
            F = num
        else :
            if num > S and num != F:
                S = num
    return S
print(sec_largest([1,2,3,4,5,6,7,8,99])) 

    
    