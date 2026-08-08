def greet(uname):
    print(f'hello {uname}' )

def add(x,y):
    print(f'addition of {x} and {y}={x+y}')
def addition(*nums):
    sum=0
    for num in nums:
        sum=sum+num
    print(f'the sum of {len(nums)} numbers= {sum}')
