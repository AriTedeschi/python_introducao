#conjuntos não repete valores
# conjunto = {1, 2, 3, 4, 4, 2}
# print(type(conjunto))
# print(conjunto)

# conjunto.add(5)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)

# conjunto  = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8, 9}
# conjuntoUniao = conjunto.union(conjunto2)
# print(conjunto)
# print(conjunto2)
# print(conjuntoUniao)

# conjuntoInterseccao = conjunto.intersection(conjunto2)
# print(conjunto)
# print(conjunto2)
# print(conjuntoInterseccao)

# conjuntoDiferenca = conjunto.difference(conjunto2)
# print(conjunto)
# print(conjunto2)
# print(conjuntoDiferenca)

# conjuntoDiferencaSimetrica = conjunto.symmetric_difference(conjunto2)
# print(conjuntoDiferencaSimetrica)

conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}
conjuntoSubset = conjuntoB.issubset(conjuntoA)
print('Conjunto B é subconjunto de A? {}'.format(conjuntoSubset))

conjuntoSuperset = conjuntoB.issuperset(conjuntoA)
print('Conjunto B é superconjunto de A? {}'.format(conjuntoSuperset))

lista = ['cachorro', 'cachorro', 'gato', 'elefante', 'elefante']
conjunto_animais = set(lista)
print(lista)
print(conjunto_animais)
lista = list(conjunto_animais)
print('lista {}'.format(lista))
print('conjunto {}'.format(conjunto_animais))

# conjunto_a = {1, 1, 3, 4, 5}
# conjunto_b = {1, 3, 6}
# conjunto_a.add(6)
# conjunto_a.remove(1)
# resultado = list(conjunto_a.intersection(conjunto_b))
# print(resultado)
conjunto1 = {4, 8, 12, 16}
conjunto2 = {5, 10, 15, 20}
print(conjunto1.union(conjunto2))