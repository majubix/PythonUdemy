idade = int(input('Digite sua idade: '))

if idade >=16:
    print('Voto permitido')
elif idade < 0 :
    print('idade invalida')
else:
    print('Menor de idade nao pode votar')