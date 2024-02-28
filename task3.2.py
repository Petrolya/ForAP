a = ''
s = ''
while a != 'stop':
    a = input('Введите слово ')
    s = s + a + ' '
print(s[:-5])