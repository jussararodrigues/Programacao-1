from funcoes import *

arquivoUsuarios = open("usuarios.txt", "r")
#Carrega a lista de marcadores de usuários descriptografada
marcadoresUsuarios = carregarMarcadores(arquivoUsuarios, descriptografia)
#Cria o dicionário de usuários descriptografado
dicionarioUsuarios = carregarDicionario(arquivoUsuarios, descriptografia, funcaoDicionario)


arquivoElementos = open("elementos.txt", "r")
#Carrega a lista de marcadores de livros descriptografada
marcadoresLivros = carregarMarcadores(arquivoElementos, descriptografia)
#Cria o dicionário de livros descritografado
dicionarioElementos = carregarDicionario(arquivoElementos, descriptografia, funcaoDicionario)

arquivoLogs = open("log.txt", "r")
dicionarioLogs = {}

#Cria o dicionário de Logs de ações
condicao = True
while condicao:
    linha = arquivoLogs.readline()
    if linha != "" and linha != " " and linha != "\n":
        linha = linha.strip()
        listaLogs = linha.split(" , ")
        dicionarioLogs = capturarLogsAcoes(listaLogs[0], listaLogs[1], listaLogs[2] + " " + listaLogs[3], dicionarioLogs)
    else:
        condicao = False
