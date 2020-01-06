def is_armstrong_number(number):
    test = 0
    for digit in str(number):
        test += int(digit) ** int(len(str(number)))
    print(test)
    if number == test:
        return True
    else:
        return False
is_armstrong_number(153)
