print("Поиск счастливого билета")
number = abs(int(input("Введите номер вашего билета: ")))
numberOfDigit = 6 # количество цифр билетика
n = str(number)
if (len(str(number)) == numberOfDigit):
    leftSum = int(n[0]) + int(n[1]) + int(n[2])
    rightSum = int(n[3]) + int(n[4]) + int(n[5])
    if (leftSum == rightSum):
        print("Поздравляю, вы обладатель счастливого билета!")
    else:
        print("Билет не счастливый, в следующий раз повезёт!")
else:
    print("На российских проездных билетах обычно 6 цифр!")
