num1=int(input('enter number1:'))
num2=int(input('enter number2:'))

choice=input("which arithmetic operation you choose to perform (+,-,/,*)")

if choice== '+':
    print(f'result={num1+num2}')
elif choice== "-":
    print(f'result={num1-num2}')
elif choice== "/":
    if num2==0:
        print('not divisible by zero')

    else:

     print(f'result={num1/num2}')

elif choice== "*":
    print(f'result={num1*num2}')
else:
    print('invalid choice')
