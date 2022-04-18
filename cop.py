a = int(input('a: '))
b = int(input('b: '))
x = input('znak: ')

if x == '+':
    print(a+b)
elif x == '-':
    print(a-b)
elif x == '*':
    print(a*b)
elif x == '/':
    print(a/b)
elif x == '%':
    print(a%b)
else:
    print('Неизвестный знак')
