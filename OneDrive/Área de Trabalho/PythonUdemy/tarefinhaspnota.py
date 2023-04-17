#slide 01 
#questao 1

def encontra_pares_inversos(lista_palavras):
    pares_inversos = []
    for i in range(len(lista_palavras)):
        for j in range(i+1, len(lista_palavras)):
            if lista_palavras[i][::-1] == lista_palavras[j] and (lista_palavras[j], lista_palavras[i]) not in pares_inversos:
                pares_inversos.append((lista_palavras[i], lista_palavras[j]))
    return pares_inversos


lista = ['amor', 'roma', 'ovo', 'pato', 'topo', 'sol', 'los', 'lobo']
print(encontra_pares_inversos(lista))

    