#multiplos operadores de comparação
#codigo mais limpo
#if valor_produto >= 20 and valor_produto <40:
#melhor opção:

valor_produto = float(input('Digite o valor do seu produto: '))


if 20 <= valor_produto < 40:
    print('O produto foi aceito para publicar!')
else:
    print('Não foi aceito!')