#FUNÇÕES DE CRIPTOGRAFIA -------------------------------------------------------------------------------

#Criptografia
def salvarArquivoCriptografia(dicElemUsers, arquivo, marcadores):
    '''Esta função criptografa todos os dados presentes em um determinado
    dicionário e salva-os no arquivo correspondente.'''
    contador = 0
    for marcador in marcadores:
        contador += 1
        for char in marcador:
            char = str(ord(char) + 37)
            arquivo.write(char)
            arquivo.write(" ")
                
        if contador != len(marcadores):
            arquivo.write(", ")

    arquivo.write("\n")
        
    for elemento in dicElemUsers:
        for char in elemento:
            char = str(ord(char) + 37)
            arquivo.write(char)
            arquivo.write(" ")
            
        arquivo.write(", ")
        contador = 0
        for atributo in dicElemUsers[elemento]:
            contador += 1
            for char in atributo:
                char = str(ord(char) + 37)
                arquivo.write(char)
                arquivo.write(" ")
                
            if contador != len(dicElemUsers[elemento]):
                arquivo.write(", ")

        arquivo.write("\n")

    arquivo.close()

    return arquivo

#Descriptografia
def descriptografia(linha):
    '''Esta função retorna a string descriptografada
    correspondente a linha do arquivo.'''
    caracteres = linha.split()
    palavras = []
    palavra = ""
    contador = 0

    for char in caracteres:
        contador += 1
        if char != ",":
            char = int(char)
            char = chr(char - 37)
            palavra += char

            if contador == len(caracteres):
                palavras.append(palavra)

        else:
            palavras.append(palavra)
            palavra = ""

    return palavras

#FUNCIONALIDADES DO SISTEMA -----------------------------------------------------------------------------

#Ordenação de Elementos
def ordenarElementos(autores, dicElementos, posicao, listaMarcadores, funcaoPrint, funcaoDic):
    '''Esta função faz uma varredura por todo o dicionário e imprime,
    de forma ordenada (de acordo com o autor e a ordem alfabética de seu nome),
    todos os livros cadastrados no sistema.'''
    marcadoresNovos = ["Autor"]
    for marcador in listaMarcadores:
        if marcador != "Autor":
            marcadoresNovos.append(marcador)
                        
    autores.sort()
    autor = ""
    while len(autores) > 0:
        for elemento in dicElementos:
            listaElemento = []
            if dicElementos[elemento][posicao] == autores[0]:
                if dicElementos[elemento][posicao] != autor:
                    autor = dicElementos[elemento][posicao]
                    print("." * 40)
                    print(marcadoresNovos[0].upper() + ": " + autor.upper())
                listaElemento.append(dicElementos[elemento][posicao])
                listaElemento.append(elemento)
                contador = 0
                for atributo in dicElementos[elemento]:
                    if contador != posicao:
                        listaElemento.append(atributo)
                                    
                    contador += 1

            if len(listaElemento) > 0:
                dicionarioOrdenados = {}
                dicionarioOrdenados = funcaoDic(listaElemento, dicionarioOrdenados)
                imprimir = funcaoPrint(marcadoresNovos, dicionarioOrdenados)
                            
        del autores[0]
            
#Busca por Elemento
def buscarElemento(funcaoDeFiltro, dicElementos, dicFiltrados, listaMarcadores):
    '''Esta função organiza as buscas filtradas que são realizadas através
    da função "funcaoFiltrar" e aplica-a quantas vezes precisar,
    de acordo com a quantidade de filtros que o usuário desejar utilizar.'''
    r = input("\nDeseja fazer a busca pelo " + listaMarcadores[0] + " (s/n)? ")
    while r != "s" and r != "n":
        print("\nOPÇÃO INVÁLIDA")
        r = input("\nDeseja fazer a busca pelo " + listaMarcadores[0] + " (s/n)? ")
        
    if r == "s":
        chave = input("\nDigite o " + listaMarcadores[0] + " do cadastro que deseja buscar: ")
        print("")
        contador = 0

        while chave not in dicElementos:
            chave = input("Não possuímos nenhum livro com este " + listaMarcadores[0] + ", insira outro: ") 

        dicFiltrados[chave] = dicElementos[chave]
                                    
    else:
        condicao = True
        while condicao:
            quantidade = input("\nQuantos filtros deseja utilizar (Mínimo 2)? ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                if quantidade >= 2:
                    condicao = False

        dicFiltrados = dicElementos
        for num in range(quantidade):
            filtros = []
            tipoFiltro = input("\nDigite o tipo de filtro desejado: ")
            filtro = input("Digite o filtro: ")
            filtros.append(tipoFiltro)
            filtros.append(filtro)
            dicFiltrados = funcaoDeFiltro(filtros, listaMarcadores, dicFiltrados)

    return dicFiltrados

#Cadastro de Elemento
def cadastrarElemento(dicElementos, listaMarcadores):
    '''Esta função organiza os dados, através de uma lista, para cadastro
    fornecidos pelo usuário e coloca-os no dicionário correspondente,
    para serem salvos no arquivo correspondente quando o sistema for finalizado.'''
    listaCadastro = []
    chave = input("\nInsira o " + listaMarcadores[0] + " : ")
    while chave in dicElementos:
        chave = input("\nJá possuímos um livro com este " + listaMarcadores[0] + ", insira outro: ")
    
    print("")
    for num in range(len(listaMarcadores) - 1):
        cadastrar = input(listaMarcadores[num + 1] + ": ")
        listaCadastro.append(cadastrar)

    listaCadastro = tuple(listaCadastro)
    dicElementos[chave] = listaCadastro
    print("\nLivro", dicElementos[chave][0], "cadastrado com sucesso!\n")
    
    return dicElementos

#Cadastro de Usuário
def cadastrarUsuario(dicUsuarios, listaMarcadores):
    '''Esta função organiza os dados para cadastro de um novo usuário,
    através de uma lista (onde é adicionado ao final da mesma
    o tipo de usuário "estagiario"), que são fornecidos pelo usuário que está logado
    no sistema e coloca-os no dicionário correspondente, para serem salvos no arquivo
    correspondente quando o sistema for finalizado.'''
    listaCadastro = []
    chave = input("\nInsira o " + listaMarcadores[0] + ": ")
    while chave in dicUsuarios:
        chave = input("\nJá possuímos cadastro com este " + listaMarcadores[0] + ", insira outro: ")

    print("")
    for num in range(len(listaMarcadores) - 2):
        cadastrar = input(listaMarcadores[num + 1] + ": ")
        listaCadastro.append(cadastrar)

    listaCadastro.append("estagiario")
    listaCadastro = tuple(listaCadastro)

    dicUsuarios[chave] = listaCadastro
    print("\nUsuário", chave, "cadastrado com sucesso!")
    
    return dicUsuarios

#Remoção de Cadastro
def removerElemento(dicElemUsers, listaMarcadores):
    '''Esta função remove do dicionário correspondente o elemento que o usuário
    deseja remover, sendo identificado através da chave passada pelo mesmo.'''
    chave = input("\nInsira o " + listaMarcadores[0] + " do cadastro que deseja remover: ")
    while chave not in dicElemUsers:
        chave = input("Não possuimos nada cadastrado com este " + listaMarcadores[0] + ", insira outro: ")

    titulo = dicElemUsers[chave][0]
    apagar = input("\nDeseja excluir o cadastro de " + titulo + " (s/n)? ")
    if apagar == "s":
        dicElemUsers.pop(chave)
        print("\n\nO cadastro de", titulo, "foi excluído com sucesso!")
    else:
        print("\n\nO cadastro de", titulo, "não foi excluído.")

#Alteração de Cadastro
def alterarCadastro(dicElemUsers, listaMarcadores):
    '''Esta função altera o cadastro de algo que está no dicionário,
    removendo este cadastro atual e adicionando um novo, com as novas
    informações passadas pelo usuário.'''
    chave = input("Insira o " + listaMarcadores[0] + " do cadastro que deseja alterar: ")

    while chave not in dicElemUsers:
        chave = input("Não possuímos nenhum cadastro com este " + listaMarcadores[0] + ", insira outro: ")

    alterados = []
    contador = 0
    for num in range(len(dicElemUsers[chave])):
        print("")
        print(listaMarcadores[num + 1] + " atual: " + dicElemUsers[chave][contador])
        alterar = input("Novo(a) " + listaMarcadores[num + 1] + ": ")
        alterados.append(alterar)
        contador += 1

    titulo = dicElemUsers[chave][0]
    alterar = input("\nTem certeza que deseja alterar o cadastro de " + titulo + "(s/n)? ")
    if alterar == "s":
        alterados = tuple(alterados)
        dicElemUsers[chave] = alterados
        print("\n\nAlteração do cadastro de '" + titulo + "' realizada com sucesso!")
    elif alterar == "n":
        print("\n\nAlteração não realizada, os dados continuam os mesmos.")

    return dicElemUsers

##Alteração de Nível de Acesso
def alterarNivelAcesso(dicUsuarios):
    '''Esta função altera o nível de acesso de um determinado usuário,
    adicionando os demais dados do mesmo em uma lista, assim como o seu novo nivel
    de acesso, transformando-a depois em uma tupla e readicionando ao dicionário correspondente.'''
    chave = input("\nDigite o login do usuário que deseja alterar o nível de acesso: ")
    while chave not in dicUsuarios:
        chave = input("Não possuímos nenhum usuário com este login, por favor, insira outro: ")

    print("\n\nUsuário", dicUsuarios[chave][0], "encontrado.\n")
    listaUsuario = []
    tiposUsuarios = ['estagiario', 'tecnico', 'gerente', 'superusuario']
    contador = 0
    for elem in dicUsuarios[chave]:
        if contador == len(dicUsuarios[chave]) - 1:
            print("\nDigite o novo tipo de acesso deste Usuário:\n")
            for tipo in tiposUsuarios:
                print(tipo)

            alterar = input("\nResposta: ")
            print("")
            while alterar not in tiposUsuarios:
                alterar = input("Não possuímos esta opção, escolha outra: ")
                
            listaUsuario.append(alterar)

        else:
            listaUsuario.append(elem)
                
        contador += 1

    nome = dicUsuarios[chave][0]
    dicUsuarios[chave] = tuple(listaUsuario)
    print("\n\nNível de acesso de " + nome + " alterado para " + alterar + ".")

    return dicUsuarios

#Busca e Impressão de Logs
def buscarLogs(marcadores, dicLogs, busca):
    '''Busca as ações realizadas no sistema de acordo com a opção selecionada
    pelo usuário (Data ou Login) e depois as imprime, de forma organizada e legível.'''
    if busca == 1:
        login = input("\nInsira o login para realizar a busca: ")
        if login in dicLogs:
            for lista in dicLogs[login]:
                print("." * 70)
                contador = 0
                print(marcadores[contador] + ": " + login)
                for elemento in lista:
                    contador += 1
                    print(marcadores[contador] + ": " + elemento)

    else:
        data = input("\nInsira a data para realizar a busca (No formato DD-MM-AAAA): ")
        for cadastro in dicLogs:
            for lista in dicLogs[cadastro]:
                if lista[1] == data:
                    print("." * 70)
                    contador = 0
                    print(marcadores[contador] + ": " + cadastro)
                    for elemento in lista:
                        contador += 1
                        print(marcadores[contador] + ": " + elemento)

#OUTRAS FUNÇÕES ------------------------------------------------------------------------------

#Adição de elementos em um dicionário já existente
def funcaoDicionario(lista, dicionario):
    '''Esta função adiciona a lista de palavras de uma
    determinada linha de um arquivo em dicionario.'''
    chave = lista[0]
    del lista[0]
    dicionario[chave] = tuple(lista)

    return dicionario

#Filtração de Buscas
def funcaoFiltrar(listaFiltros, listaMarcadores, dicionario):
    '''Esta função filtra a busca por um determinado livro,
    onde o filtro é fornecido pelo usuário,
    realizando esta busca através de um único filtro por vez.'''
    dicFiltros = {}
    contadorFuncao = 0
    posicao = 0
    for marcador in listaMarcadores:
        if marcador == listaFiltros[0]:
            posicao = contadorFuncao

        contadorFuncao += 1
        
    for chave in dicionario:
        if dicionario[chave][posicao-1] == listaFiltros[1]:
            dicFiltros[chave] = dicionario[chave]
    
    return dicFiltros

#Impressão de dados de forma organizada
def funcaoPrintar(listaMarcadores, dicionario):
    '''Esta função imprime os dados de um dicionário de forma organizada.'''
    for chave in dicionario:
        print("." * 40)
        contadorFuncao = 1
        for elem in dicionario[chave]:
            print(listaMarcadores[contadorFuncao] + ": " + elem)
            contadorFuncao += 1

#Captura das ações dos usuários no sistema
def capturarLogsAcoes(login, acao, horario, dicionario):
    '''Esta função captura as ações (incluindo login e horário) realizadas pelos
    usuários no sistema, organizando-as e salvando-as no dicionário correspondente.'''
    horario = horario.split()
    data = horario[0]
    listaData = data.split("-")
    if len(listaData[0]) == 4:
        data = listaData[2] + "-" + listaData[1] + "-" + listaData[0]

    hora = horario[1]
    listaHora = hora.split(".")
    hora = listaHora[0]

    if login in dicionario:
        fez = (acao, data, hora)
        dicionario[login].append(fez)
    else:
        fez = (acao, data, hora)
        dicionario[login] = [fez]

    return dicionario

#Gravação em arquivo dos dados relativos aos logs de ação 
def salvarLogsArquivo(dicionario, arquivo):
    '''Esta função recebe o dicionário dos logs e armazena os
    dados presentes no mesmo em um arquivo correspondente.'''
    for elemento in dicionario:
        for lista in dicionario[elemento]:
            arquivo.write(elemento)
            arquivo.write(" , ")
            contador = 0
            for atributo in lista:
                contador += 1
                arquivo.write(atributo)
                if contador != len(lista):
                    arquivo.write(" , ")

            arquivo.write("\n")

    return arquivo

#Carregamento de Marcadores
def carregarMarcadores(arquivo, funcaoDescriptografia):
    '''Carrega e descriptografa os marcadores presentes na
    primeira linha do arquivo em questão.'''
    linha = arquivo.readline()
    listaMarcadores = tuple(descriptografia(linha))

    return listaMarcadores

#Carregamento de Dicionário
def carregarDicionario(arquivo, funcaoDescriptografia, funcaoDic):
    '''Carrega e descriptografa os dados presentes no arquivo em questão
    e os organiza em um dicionário.'''
    dicionario = {}
    condicao = True              
    while condicao:
        linha = arquivo.readline()
        if linha != "" and linha != " " and linha != "\n":
            listaDescriptografada = funcaoDescriptografia(linha)
            dicionario = funcaoDic(listaDescriptografada, dicionario)
        else:
            condicao = False

    return dicionario
