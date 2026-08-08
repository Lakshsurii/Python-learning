num=int(input('enter a nujmber='))
for x in range(num,num+4):
    for y in range(1,11):
        t=x*y
        print(f'{x}*{y}={t}',end='\t')
    print()
