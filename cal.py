# A python program to perform basic calculator operations using funtions
n1 = 2
n2 = 3
def add(x, y):
    return x + y
def subt(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
print('Select operation: ')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
c = input('Enter the choice: ')
if c == '1':
    print('ans = ', add(n1,n2))
elif c == '2':
    print('ans = ', subt(n1, n2))
elif c == '3':
    print('ans = ', mul(n1, n2))
elif c == '4':
    print('ans = ', div(n1, n2))
else:
    print('Invalid option')