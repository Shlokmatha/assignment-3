1)
number = int(input('Write a number: \n'))
print(bin(number))



2)
# calculator
calculate = input('Enter expression to calculate : \n\t')
print(eval(calculate))



3)
# import math
# part(a)
# --> (3+4)*5

# part(b)
# --> n*(n-1)/2

# part(c)
# --> 4*math.pi*r**2

# part(d)
# --> math.sqrt(r*(math.cos(a)**2 + r*(math.sin(b)**2))

# part(e)
# --> (y2-y1)/(x2-x1)



4)
# part(a)
print('part(a)')
for i in range(5):
    print(i)

# part(b)
print('part(b)')
for i in range(3,10):
    print(i)

# part(c)
print('part(c)')
for i in range (4,13,3):
    print(i)

# part(d)
print('part(d)')
for i in range (15,5,-2):
    print(i)

# part(e)
print('part(e)')
for i in range (5,3):
    print(i)



5)
Hydrogen = float(input('Enter number of H atoms : \n \t'))
Oxygen = float(input('Enter number of O atoms : \n \t'))
Carbon = float(input('Enter number of C atoms : \n \t'))

molecular_wt = (Hydrogen*1.007944 + Carbon*12.0107 + Oxygen*15.9994)
print(f'molecular weight of the compound is {molecular_wt}')



























