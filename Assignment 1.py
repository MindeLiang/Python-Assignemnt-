

number_1 = float(input("please enter a number: "))
number_2 = float(input("please enter a number: "))

print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
try:
    print(number_1 / number_2)
    print(number_1 % number_2)
except ZeroDivisionError:
    print('Zero cannot be Division')
    print('Zero cannot be Division')
print(number_1 ** number_2)