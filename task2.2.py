print('Введите номер места')
num = int(input())
if num % 2 == 0 and num >=37 and num <=54:
    print('Это верхнее боковое место')
elif num % 2 != 0 and num >=37 and num <=54:
    print('Это нижнее боковое место')
elif num % 2 == 0 and num <=37 or num >=54:
    print('Это верхнее место в купе')
elif num % 2 != 0 and num <=37 or num >=54:
    print('Это нижнее место в купе')