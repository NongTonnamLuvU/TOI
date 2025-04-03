Money = int(input(""))  
Coin = [10, 5, 2, 1] 
for i in Coin:
    amounts = Money // i 
    Money %= i
    print(f"{i} = {amounts}")
