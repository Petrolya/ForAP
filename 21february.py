n = int(input('Введите кол-во слов'))
s = ''
while n>0:
    a = input()
    s = s + a + ' '
    n=n-1
print('Итоговая строка:', s)