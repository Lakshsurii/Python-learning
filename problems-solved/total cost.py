choice = int(input("enter the number of items to purchase: "))
total = 0

for i in range(1,choice+1):
    price = float(input(f"Enter Price of {i}: "))
    total=total+price
print(f"The total cost of your purchase is: {total}")
    
