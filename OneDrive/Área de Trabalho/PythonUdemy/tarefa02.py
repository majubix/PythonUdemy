a = int(input('Digite a primeira nota: '))
b = int(input('Digite a segunda nota: '))
c = int(input('Digite a ultima nota'))
media = (a + b + c)/3

if media < 7:
    print('Recuperação!')
elif media == 7 :
    print('quase nao passa')
else:
    print('muito bem!')
