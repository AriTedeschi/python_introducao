exibe_lista = lambda lista: [print(x) for x in lista]

def escrever_texto(texto):
    #sobreescreve
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    alunos_notas = arquivo.read()
    alunos_notas = alunos_notas.split('\n')
    for x in alunos_notas:
        lista_notas = x.split(',')[1:]
        aluno = x.split(',')[0]
        print('Aluno: {} notas : {}'.format(aluno, lista_notas))
        
        media = lambda notas: sum([int(i) for i in lista_notas])/len(lista_notas)
        print('Aluno: {} media : {}'.format(aluno, media(lista_notas)))

    exibe_lista(alunos_notas)

def copia_arquivo(nome):
    import shutil
    shutil.copy(nome, 'path')

def move_arquivo(nome):
    import shutil
    shutil.move(nome, 'path')

if __name__ == '__main__':
    # escrever_texto('Primeira Linha.\n')
    # escrever_texto('Segunda Linha.\n')
    # atualizar_arquivo(' Terceira Linha.\n')
    # ler_arquivo('teste.txt')
    # atualizar_arquivo('Felipe, 7, 8, 5, 6\n')
    # atualizar_arquivo('Cesar, 7, 9, 3, 8\n')
    media_notas('teste.txt')