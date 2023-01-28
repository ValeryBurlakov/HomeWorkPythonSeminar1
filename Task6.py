print("Поиск счастливого билета")
number = int(input("Введите номер вашего билета: "))
number2 = abs(number)
numberOfDigit = 6 # количество цифр билетика

if (len(str(number2)) == numberOfDigit):
    leftDigits = 0
    rightDigits = 0
    for i in range(numberOfDigit):
        if i < 3:
            leftDigits += number2 // 10 ** i % 10
        else:
            rightDigits += number2 // 10 ** i % 10
    if (leftDigits == rightDigits):
        print("Поздравляю, вы обладатель счастливого билета!")
    else:
        print("Билет не счастливый, в следующий раз повезёт!")
else:
    print("На российских проездных билетах обычно 6 цифр!")
