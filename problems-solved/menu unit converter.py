print('conversion menu')
print("1.fahrenheit to celsius")
print("2.celsius to fahrenheit")
print("3.centimeters to inches")
print("4.inches to centimeters")

choice=int(input("enter your choice (1-4): "))

if choice==1:
      fahrenheit = float(input("Enter temperature in Fahrenheit: "))
      celsius = (fahrenheit - 32) * 5 / 9
      print("temperature in celsius: ", celsius)
      
      
elif choice==2:
    celsius=float(input("Enter temperature in celsius: "))
    fahrenheit=(celsius* 9/5) + 32
    print(" Temperature in Fahrenheit: ",fahrenheit)

elif choice==3:
     centimeters = float(input("Enter length in centimeters: "))
     inches = centimeters / 2.54
     print("Length in inches:", inches)
elif choice==4:
    inches = float(input("Enter length in inches: "))
    centimeters = inches * 2.54
    print("Length in centimeters:", centimeters)
else:
    print("invalid choice")
    
           
