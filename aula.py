""" diretorio = 'C:/ """


def escrever_arquivo(texto):
    
    arquivo = open ('Notas_alunos', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open (nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open (nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    pass

if __name__=='__main__':   
    media_notas = ('notas.txs')

    """escrever_arquivo('Primeira linha./n')"""
    """ aluno = 'Cesar,7,9,3,8 /n' """
    """ atualizar_arquivo('notas.txt',aluno) """
    """ ler_arquivo('teste.txt') """