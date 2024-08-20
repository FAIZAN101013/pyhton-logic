prices = [10, 20 , 30 ]
'''total = sum(prices)
for i in prices:
        print(f"{total}")
        break'''
total = 0
for i in prices:
    total += i
for i in prices:
    print(f"{total}")
    break
    