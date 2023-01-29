print("Нахождение суммы цифр трёхзначного числа. Задача 2:")
number = abs(int(input("Введите трёхзначное число: ")))
index = 3 

oneElement = int(number / 100)
twoElement = int((number / 10) % 10)
threeElement = int(number % 10)

if (len(str(number)) == index):
    print(oneElement + twoElement + threeElement)

else:
    print("Вы ввели не трёхзначное число!")
