import random
er = 0
k=0
while er<3:
    fsop = random.randint(1, 10)
    secop = random.randint(1, 10)
    answer=int(input(f'Решите пример:{fsop}+{secop}='))
    if answer == (fsop+secop):
        print('Правильно!')
        k = k+1
    else:
        print('Ответ неверный')
        er=er+1
print('Игра окончена')
print('Правильных ответов:',k)

