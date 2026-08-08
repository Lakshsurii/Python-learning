num=int(input('enter a number'))
t=num
f=1
while num>0:
    f=num*f
    num=num-1
print(f'factorial of {t}={f}')
