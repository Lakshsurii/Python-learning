print("select the shape you want to print")
print("1. Right angled triangle")
print("2. Inverted triangle")
print("3. square")
print("4. pyramid")

choice=input("Enter the shape to print(1-4): ")

if choice=="1":
    for i in range(1,5):
        print("*"*i)
        
elif choice=="2":
    for i in range(5,0,-1):
        print("*"*i)
        
elif choice=="3":
    for i in range(1,5):
        print("*"*4)
        
elif choice=="4":
    for i in range(1,5):
        print(" " *(4 - i)+"*"*((2*i)-1))    
else:
    print("Enter a valid option")
