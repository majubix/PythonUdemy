
with open('palavras.txt', 'r') as palavras:
    maior = ''
    for linha in palavras:
        if(len(linha) > len(maior)):
            maior = linha

    print(maior)