def contador_letras(lista_palavras):
    contador = [];
    for x in lista_palavras:
        qtd = len(x)
        contador.append(qtd)
    return contador

def testar():
    print('teste\n\n')

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))