#Loop com If e Else
#break para parar no if e nap repetir o if e o else

compra_confirmada = False
dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break
    else:
        print('Falha na compra!')
        break
