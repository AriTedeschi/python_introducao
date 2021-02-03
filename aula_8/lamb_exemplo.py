contador_letras = lambda lista: [len(x) for x in lista] #devolve uma lista
exibe_lista = lambda lista: [print(x) for x in lista]
soma_lam = lambda a, b: a+b

#dicionário
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}


if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'lagarto', ['viuva negra', 'aranha marrom']]
    # print(contador_letras(lista))
    # exibe_lista(lista)
    # print(soma_lam(5,3))

    # print(type(calculadora))
    # soma = calculadora['soma']
    # multiplicacao = calculadora['multiplicacao']
    # print(multiplicacao(5,7))

# valida_numero = {
#     'par': lambda a: True if a % 2 == 0 else False,
#     'impar': lambda b: True if b % 2 == 0 else False
# }
# resultado = valida_numero['par'](10)
# print(resultado)