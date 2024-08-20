'''def main():

    Weight = int(input('Enter Weight in kg'))
    Newweight = conver(Weight)
    print(f'Your Weight in l is {Newweight}')
 
def conver(Weight):
     F = Weight * 2.205
     return F
 
main()'''

weight = int(input("Enter you Weight: "))
unit = input('l for pounds anf kg for kilo ').lower()
if unit == "l" :
    nw = weight/ 2.2
    print(f'Your Weight In kilos  is {nw} kg')
else:
    unit == "k" 
    nw = weight * 2.2
    print(f'Your Weight In pounds  is {nw} l')
    