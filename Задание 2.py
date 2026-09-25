a, b, c = map(int, input("Введите три целых числа через пробел: ").split())
num1 = a*b
num2 = b*c
num3 = c*a

a_num4 = a**4
b_num5 = b%c
c_num6 = c // a
print("a*b=",num1)
print("b*c=",num2)
print("c*a=",num3)

print("a**4=",a_num4)
print("b%c=",b_num5)
print("с*a=",c_num6)

print("Сумма переменных из пункта 5 =", a_num4 + b_num5 + c_num6)
