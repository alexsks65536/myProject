print('Решаем уравнение a•x²+b•x+c=0')
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))

discriminant = b**2 - 4*a*c
print(f'Дискриминант = {discriminant}')
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f'x₁ = {x1}')
    print(f'x₂ = {x2}')

