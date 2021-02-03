# lista = [1,10]
# try:
#     arquivo = open('teste.txt', 'r')
#     texto = arquivo.read()
#     # divisao = 10/0
#     # numero = lista[3]
#     # x = a
# except BaseException as ex:
#     #Identifica erro
#     print('Erro Desconhecido, Erro: {}'.format(ex))
# except Exception as ex:
#     #Identifica erro
#     print('Erro Desconhecido, Erro: {}'.format(ex))
# except ZeroDivisionError:
#     print('Não é possível realizar uma divisão por 0')
# except IndexError:
#     print('Erro ao acessar um indice inválido da lista')
# except :
#     print('Erro Desconhecido')
# else:
#     print('Executa quando não ocorre exceção')
# finally:
#     print('Sempre executa')
#     print('Fechando o arquivo...')
#     arquivo.close()

# try:
#     x = int(input('Entre com uam nota de 0 a 10: '))
#     print(x)
# except ValueError:
#     print('Valor inválido, deve-se digitar apenas números')
# try:    
#     divisao = 10 / 0
# except ArithmeticError:
#     erro = 'Houve um erro ao realizar uma operação aritmética'
# except Exception:
#     erro = 'Ocorreu um erro desconhecido'
# else:
#     erro = False    
# finally:
#     if erro:
#         print(erro)
#     else:
#         print(divisao)

# try:
#     lista = [1, 2]
#     print(lista[2])
# except Exception:
#     print('Ocorreu um erro desconhecido')
# except IndexError:
#     print('Não foi possível acessar o index pois ele não existe na lista')