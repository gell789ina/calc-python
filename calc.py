s = input("Введите знак ( + - * / ^) или корень: ")
a = float(input('a = '))
b = float(input('b = '))

if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    print(a / b)
elif s == '^':
    print( a ** b)
elif s == 'корень':
    print( a ** 0.5)