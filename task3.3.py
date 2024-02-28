k=0
while True:
    word = input('Введите слово')
    for s in word:
        if s == 'ф' or s == 'Ф':
            k=k+1
    if k>0:
        print('Ого! Это редкое слово!')
        k = 0
    else:
        print('Эх, это не очень редкое слово...')
