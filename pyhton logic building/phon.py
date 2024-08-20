dic = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"

}

num = int(input(":"))
for num in dic:
    print(dic.get(num,"Done"), end=" " )# end= output on the same line
    
####################################################################################################

num = input("Enter a number: ")
output = " ".join(dic[digit] for digit in num) #" ".join(...) joins the words with a space in between to ensure all the words are printed on the same line.
print(output)
    