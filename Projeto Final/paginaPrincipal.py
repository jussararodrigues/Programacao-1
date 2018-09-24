from funcoes import *
from carregarDicionarios import *
from datetime import datetime

continuar = "s"
while continuar == "s":
    print("")
    print("-" * 10, "BEM VINDO AO SISTEMA DA BIBLIOTECA VIAGEM À LEITURA", "-" * 10)

    condicao = False
    tipoUsuario = ""
    while condicao == False:
        login = input("\nInsira o seu login: ")
        senha = input("\nInsira a sua senha: ")

        if login in dicionarioUsuarios:
            if senha == dicionarioUsuarios[login][1]:
                condicao = True
                tipoUsuario = dicionarioUsuarios[login][2]
                acao = "Login no sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            else:
                print("\nxxxxx LOGIN OU SENHA INVÁLIDOS xxxxx\n")
                print("." * 60)

        else:
            print("\nxxxxx LOGIN OU SENHA INVÁLIDOS xxxxx\n")
            print("." * 60)
            

    print("")
    if tipoUsuario == "estagiario":
        resposta = 0
        while resposta != 2:
            print("-" * 17, "BEM VINDO A PÁGINA DO ESTAGIÁRIO", "-" * 17)
            print("\nEscolha uma das opções abaixo:")
            print("\n1. Buscar um Livro\n2. Deslogar\n")
            resposta = input("Resposta: ")
            if resposta.isdigit():
                resposta = int(resposta)

            if resposta == 1:
                print("-" * 20, "BUSCA DE LIVROS", "-" * 20)
                print("")
                filtrar = "s"
                while filtrar == "s":
                    dicionarioFiltrados = {}
                    dicionarioFiltrados = buscarElemento(funcaoFiltrar, dicionarioElementos, dicionarioFiltrados, marcadoresLivros)
                    acao = "Busca por livro"
                    horario = str(datetime.now())
                    logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

                    if len(dicionarioFiltrados) > 0:
                        printar = funcaoPrintar(marcadoresLivros, dicionarioFiltrados)

                    else:
                        print("\nInfelizmente, não possuímos nenhum livro com esses atributos.")

                    filtrar = input("\n\nDeseja fazer uma nova busca (s/n)? ")
                    print("")
                

            elif resposta == 2:
                acao = "Logout do sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                print("\nDeslogando...\n")

            else:
                print("\nOpção Inválida.\n")

    elif tipoUsuario == "tecnico":
        resposta = 0
        while resposta != 3:
            print("-" * 15, "BEM VINDO À PÁGINA DO TÉCNICO", "-" * 15)
            print("\nEscolha uma das opções abaixo:\n")
            print("1. Buscar um Livro")
            print("2. Cadastrar um Livro")
            print("3. Deslogar")
            resposta = input("\nResposta: ")
            if resposta.isdigit():
                resposta = int(resposta)

            if resposta == 1:
                print("-" * 20, "BUSCA DE LIVROS", "-" * 20)
                print("")
                filtrar = "s"
                while filtrar == "s":
                    dicionarioFiltrados = {}
                    dicionarioFiltrados = buscarElemento(funcaoFiltrar, dicionarioElementos, dicionarioFiltrados, marcadoresLivros)
                    acao = "Busca por livro"
                    horario = str(datetime.now())
                    logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                    
                    if len(dicionarioFiltrados) > 0:
                        printar = funcaoPrintar(marcadoresLivros, dicionarioFiltrados)

                    else:
                        print("\nInfelizmente, não possuímos nenhum livro com esses atributos.")

                    filtrar = input("\n\nDeseja fazer uma nova busca (s/n)? ")
                    print("")

            elif resposta == 2:
                print("-" * 20, "CADASTRO DE LIVRO", "-" * 20)
                print("")
                dicionarioElementos = cadastrarElemento(dicionarioElementos, marcadoresLivros)
                acao = "Cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 3:
                acao = "Logout do sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                print("\nDeslogando...\n")

            else:
                print("\nOpção Inválida.\n")

    elif tipoUsuario == "gerente":
        resposta = 0
        while resposta != 8:
            print("-" * 17, "BEM VINDO A PÁGINA DO GERENTE", "-" * 17)
            print("\nEscolha uma das opções abaixo:\n")
            print("1. Cadastrar Usuário")
            print("2. Remover Usuário")
            print("3. Cadastrar Livro")
            print("4. Buscar Livro")
            print("5. Alterar Cadastro de Livro")
            print("6. Remover Cadastro de Livro")
            print("7. Exibir Todos os Livros Ordenados")
            print("8. Deslogar")
            resposta = input("\nResposta: ")
            if resposta.isdigit():
                resposta = int(resposta)

            if resposta == 1:
                print("-" * 20, "CADASTRO DE USUÁRIO", "-" * 20)
                print("")
                dicionarioUsuarios = cadastrarUsuario(dicionarioUsuarios, marcadoresUsuarios)
                acao = "Cadastro de usuário"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 2:
                print("-" * 20, "REMOÇÃO DE CADASTRO DE USUÁRIO", "-" * 20)
                print("")
                remover = removerElemento(dicionarioUsuarios, marcadoresUsuarios)
                acao = "Remoção de cadastro de usuário"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
            
            elif resposta == 3:
                print("-" * 20, "CADASTRO DE LIVRO", "-" * 20)
                print("")
                dicionarioElementos = cadastrarElemento(dicionarioElementos, marcadoresLivros)
                acao = "Cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 4:
                print("-" * 20, "BUSCA DE LIVROS", "-" * 20)
                print("")
                filtrar = "s"
                while filtrar == "s":
                    dicionarioFiltrados = {}
                    dicionarioFiltrados = buscarElemento(funcaoFiltrar, dicionarioElementos, dicionarioFiltrados, marcadoresLivros)
                    acao = "Busca por livro"
                    horario = str(datetime.now())
                    logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

                    if len(dicionarioFiltrados) > 0:
                        printar = funcaoPrintar(marcadoresLivros, dicionarioFiltrados)

                    else:
                        print("\nInfelizmente, não possuímos nenhum livro com esses atributos.")

                    filtrar = input("\n\nDeseja fazer uma nova busca (s/n)? ")
                    print("")

            elif resposta == 5:
                print("-" * 20, "ALTERAÇÃO DE CADASTRO DE LIVRO", "-" * 20)
                print("")
                dicionarioElementos = alterarCadastro(dicionarioElementos, marcadoresLivros)
                acao = "Alteração de cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                
            elif resposta == 6:
                print("-" * 20, "REMOÇÃO DE CADASTRO DE LIVRO", "-" * 20)
                print("")
                remover = removerElemento(dicionarioElementos, marcadoresLivros)
                acao = "Remoção de cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 7:
                print("-" * 20, "EXIBIÇÃO DE TODOS OS LIVROS ORDENADOS (POR AUTOR)", "-" * 20)
                print("")
                posicaoAutor = 1
                listaAutores = []
                for elemento in dicionarioElementos.values():
                    if elemento[posicaoAutor] not in listaAutores:
                        listaAutores.append(elemento[posicaoAutor])

                ordenar = ordenarElementos(listaAutores, dicionarioElementos, posicaoAutor, marcadoresLivros, funcaoPrintar, funcaoDicionario)
    
                acao = "Exibir todos os livros ordenados por autor"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)


            elif resposta == 8:
                acao = "Logout do sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                print("\nDeslogando...\n")

            else:
                print("\nOpção Inválida.\n")

    elif tipoUsuario == "superusuario":
        resposta = 0
        while resposta != 10:
            print("")
            print("-" * 17, "BEM VINDO A PÁGINA DO ADMINISTRADOR", "-" * 17)
            print("\nEscolha uma das opções abaixo:\n")
            print("1. Cadastrar Usuário")
            print("2. Remover Usuário")
            print("3. Alterar Nível de Acesso de Usuário")
            print("4. Cadastrar Livro")
            print("5. Buscar Livro")
            print("6. Alterar Cadastro de Livro")
            print("7. Remover Cadastro de Livro")
            print("8. Exibir Todos os Livros Ordenados (Por Autor)")
            print("9. Consultar Logs de Ações de Usuários")
            print("10. Deslogar")
            resposta = input("\nResposta: ")
            if resposta.isdigit():
                resposta = int(resposta)

            if resposta == 1:
                print("-" * 20, "CADASTRO DE USUÁRIO", "-" * 20)
                print("")
                dicionarioUsuarios = cadastrarUsuario(dicionarioUsuarios, marcadoresUsuarios)
                acao = "Cadastro de usuário"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 2:
                print("-" * 20, "REMOÇÃO DE USUÁRIO", "-" * 20)
                print("")
                remover = removerElemento(dicionarioUsuarios, marcadoresUsuarios)
                acao = "Remoção de cadastro de usuário"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                

            elif resposta == 3:
                print("-" * 20, "ALTERAÇÃO DE NÍVEL DE ACESSO DE USUÁRIO", "-" * 20)
                print("")
                dicionarioUsuarios = alterarNivelAcesso(dicionarioUsuarios)
                acao = "Alteração de nível de acesso ao sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 4:
                print("-" * 20, "CADASTRO DE LIVRO", "-" * 20)
                print("")
                dicionarioElementos = cadastrarElemento(dicionarioElementos, marcadoresLivros)
                acao = "Cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                
            elif resposta == 5:
                print("-" * 20, "BUSCA DE LIVROS", "-" * 20)
                print("")
                filtrar = "s"
                while filtrar == "s":
                    dicionarioFiltrados = {}
                    dicionarioFiltrados = buscarElemento(funcaoFiltrar, dicionarioElementos, dicionarioFiltrados, marcadoresLivros)
                    acao = "Busca por livro"
                    horario = str(datetime.now())
                    logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

                    if len(dicionarioFiltrados) > 0:
                        printar = funcaoPrintar(marcadoresLivros, dicionarioFiltrados)

                    else:
                        print("\nInfelizmente, não possuímos nenhum livro com esses atributos.")

                    filtrar = input("\n\nDeseja fazer uma nova busca (s/n)? ")
                    print("")

            elif resposta == 6:
                print("-" * 20, "CADASTRO DE CADASTRO DE LIVRO", "-" * 20)
                print("")
                dicionarioElementos = alterarCadastro(dicionarioElementos, marcadoresLivros)
                acao = "Alteração de cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                
            elif resposta == 7:
                print("-" * 20, "REMOÇÃO DE CADASTRO DE LIVRO", "-" * 20)
                print("")
                remover = removerElemento(dicionarioElementos, marcadoresLivros)
                acao = "Remoção de cadastro de livro"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 8:
                print("-" * 20, "EXIBIÇÃO DE TODOS OS LIVROS ORDENADOS (POR AUTOR)", "-" * 20)
                print("")
                posicaoAutor = 1
                listaAutores = []
                for elemento in dicionarioElementos.values():
                    if elemento[posicaoAutor] not in listaAutores:
                        listaAutores.append(elemento[posicaoAutor])

                ordenar = ordenarElementos(listaAutores, dicionarioElementos, posicaoAutor, marcadoresLivros, funcaoPrintar, funcaoDicionario)
    
                acao = "Exibir todos os livros ordenados por autor"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)


            elif resposta == 9:
                print("-" * 20, "CONSULTA DE LOGS DE AÇÕES", "-" * 20)
                marcadoresLogs = ("Login", "Ação", "Data", "Hora")

                buscar = "0"
                while buscar != "1" and buscar != "2":
                    print("." * 70)
                    print("\nEscolha uma das opções de busca abaixo:\n\n1. Por Login\n2. Por Data")
                    buscar = input("\nResposta: ")

                buscar = int(buscar)
                imprimir = buscarLogs(marcadoresLogs, dicionarioLogs, buscar)
                acao = "Consulta de logs de ações no sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)

            elif resposta == 10:              
                acao = "Logout do sistema"
                horario = str(datetime.now())
                logs = capturarLogsAcoes(login, acao, horario, dicionarioLogs)
                print("\nDeslogando...\n")

            else:
                print("\nOpção Inválida.\n")

    
    print("-" * 20, "LOGAR NOVAMENTE", "-" * 20)
    continuar = input("\nDeseja fazer login novamente (s/n)? ")

arquivoElementosEscrita = open("elementos.txt", "w")
salvar = salvarArquivoCriptografia(dicionarioElementos, arquivoElementosEscrita, marcadoresLivros)
arquivoUsuariosEscrita = open("usuarios.txt", "w")
salvar = salvarArquivoCriptografia(dicionarioUsuarios, arquivoUsuariosEscrita, marcadoresUsuarios)


arquivoLogsEscrita = open("log.txt", "w")
salvar = salvarLogsArquivo(dicionarioLogs, arquivoLogsEscrita)
arquivoLogsEscrita.close()
