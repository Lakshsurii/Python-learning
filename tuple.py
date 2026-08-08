tup=("krishna","shrijee","puja","akshaye","lakshit","puja")
print(tup)

print(tup[-1])

print(tup.count("puja"))
 message="betty bought a butter, but a butter was bitter"

words=message.split(sep=" ")
print(words)      

print(words.index('butter',4))

print(type(words))

words=tuple(words)
print(type(words))

borrowers=set()
borrowers.add("lakshit")
borrowers.add("om")
borrowers.add("hiten")

print('borrowers',borrowers)

depositors={'lakshit','bhawesh','om'}
print(depositors)

onlyborrowers=borrowers.difference(depositors)
print('only borrowers', onlyborrowers)

onlydepositors=depositors.difference(borrowers)
print('only depositors', onlydepositors)

commoncustomers=borrowers.intersection(depositors)
print('common cust', commoncustomers)

allcustomers= borrowers.union(depositors)
print('all customer', allcustomers)



cars='honda','city',12500
print(type(cars))


names=set(('lakshit','krishna','om','hiten'))
print()
