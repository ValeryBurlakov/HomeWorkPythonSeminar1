print("Нахождение суммы цифр трёхзначного числа. Задача 2:")
number = int(input("Введите трёхзначное число: "))
number2 = abs(number) # модуль числа
index = 3 # третий элемент

oneElement = int(number2 / 100)
twoElement = int((number2 / 10) % 10)
threeElement = int(number2 % 10)

if (len(str(number2)) > index):
    print("вы ввели не трёхзначное число!")
else:
    print(oneElement + twoElement + threeElement)