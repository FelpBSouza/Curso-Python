import shutil

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open (nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open (nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print (aluno_nota)

    aluno_nota = aluno_nota.split('\n')
    print (aluno_nota)
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        print (lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print (aluno)
        print(lista_notas)

        media = lambda notas:sum([int (i) for i in notas] )/ 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})    
    return lista_media
    print (sum(lista_notas))

def copia_arquivos(nome_arquivo):
    shutil.copy(nome_arquivo,'C:/')

def move_arquivos(nome_arquivo):
    shutil.move(nome_arquivo,''C:/)











if __name__ == '__main__': 
    move_arquivos('notas.txt')
    copia_arquivos('notas.txt')
    lista_media = media_notas('notas.txt')
    print(lista_media)
    media_notas('notas.txt')
    """ aluno = 'Mario,8,10,5,8 /n' """
    """ atualizar_arquivo('notas.txt',aluno) """