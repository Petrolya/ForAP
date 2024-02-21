color1 = input('Введите первый цвет для смешивания')
color2 = input('Введите второй цвет для смешивания')
if color1 == 'красный' and color2 == 'синий':
    print('фиолетовый')
elif color1 == 'желтый' and color2 == 'синий':
    print('зеленый')
elif color1 == 'синий' and color2 == 'синий':
    print('синий')
elif color1 == 'красный' and color2 == 'красный':
    print('красный')
elif color1 == 'желтый' and color2 == 'красный':
    print('оранжевый')
elif color1 == 'желтый' and color2 == 'желтый':
    print('желтый')
elif color1 == 'синий' and color2 == 'желтый':
    print('зеленый')
else:
    print('Ошибка')

