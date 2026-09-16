# ----- Variáveis globais ----- #
rodando = True
funcaoAtual:str = ""

# ----- Definição de Funções ----- #
funcoes = []
funcoesFavoritas = []

    #Método que cria funções da câmera com nome e descrição e as adiciona à lista de funções.
def _criarFuncao(nova_funcao: dict[str, str]):
    numFuncoes = len(funcoes)
    funcao = [nova_funcao]
    funcoes.append(nova_funcao)

_criarFuncao({'nome': "Automática", 'descricao': "Função padrão de foto."})
_criarFuncao({'nome': "Vídeo", 'descricao': "Segure o botão vermelho para iniciar a gravação."})
_criarFuncao({'nome': "Panorâmica",'descricao': "Segure o botão de foto e mova o celular para criar uma foto esticada."})
_criarFuncao({'nome': "Ler Texto",'descricao': "Aponte a câmera para qualquer texto e aperte o botão. O texto será transcrito digitalmente."})

funcoesUI = [funcoes[0], funcoes[1]]

# ----- Método para Alterar Função ----- #

funcaoAtual = funcoes[0]

def _alterarFuncao(funcao:list):
    global funcaoAtual
    funcaoAtual = funcao
    print(f"Alterando para a função {funcao['nome']}")
   

# ----- Método para Favoritar Função ----- #
def falar_usuario():
    print("Essa função é uma função padrão.")

def escolha():
    escolha = int(input("Função já favoritada. Deseja remover dos Favoritos? \n1- Sim \n2- Não \nSelecione sua opção: "))
    return escolha

def resposta_favorito():
    print(f"Favoritando a função escolhida")


def _favoritarFuncao(funcao:list):
    global funcoesFavoritas
    funcoesFavoritas = funcoesFavoritas
    
    i = 0
    if funcao['nome'] in [funcoes[0]['nome'], funcoes[1]['nome']]:
        
        chamada = falar_usuario()
        return chamada

    if len(funcoesFavoritas) > 0:
        for func in funcoesFavoritas:

            if func['nome'] == funcao['nome']:
                escolha()

                if escolha == 1:
                    funcoesFavoritas.pop(i)
                    funcoesUI.pop(i + 2)
            elif i == (len(funcoesFavoritas) - 1) and func['nome'] != funcao['nome']:
                funcoesFavoritas.append(funcao)
                funcoesUI.append(funcao)
                resposta_favorito()
                break
            i += 1
    else:
        funcoesFavoritas.append(funcao)
        funcoesUI.append(funcao)
        resposta_favorito()

# ----- Método do Menu Inicial ----- #

def _menu():
    print("O que deseja fazer?")
    print(f"1- Ver Funções \n2- Tirar Foto \n3- Alterar entre funções na UI \n4- Ver Favoritos \n5- Ver Descrição da Função Atual \n0- Encerrar Programa")
    try:
        escolha = int(input("Selecione sua opção: "))
    except ValueError:
        print("Entrada inválida! \nÉ aceito apenas números inteiros.")
    else:
        return int(escolha)

# ----- Método do Menu de Funções ----- #

def _menuFuncoes(funcao:list):
    print("--------------------------------------------------")
    print("O que deseja fazer em relação à função?")
    print(f"1- Alterar para a Função \n2- Favoritar a Função \n3- Favoritar e Alterar para a Função \n4- Ler Descrição da Função \n8- Voltar \n9- Voltar ao Menu Inicial")
    try:
        escolha = int(input("Selecione sua opção: "))
    except ValueError:
        print("Entrada inválida! \nÉ aceito apenas números inteiros.")
    else:
        match escolha:
            case 1:
                _alterarFuncao(funcao)
            case 2:
                _favoritarFuncao(funcao)
            case 3:
                _alterarFuncao(funcao)
                _favoritarFuncao(funcao)
            case 4:
                print(funcao['descricao'])
            case 8:
                _verFuncoes()
            case 9:
                return
            case _:
                print("Valor Inválido.")

# ----- Método para Ver e Selecionar Funções ----- #

def _verFuncoes():
    print("--------------------------------------------------")
    print("Selecione a função que deseja ver: ")

    for opcoes in funcoes:
        print(f"{funcoes.index(opcoes) + 1}- {opcoes['nome']}")
    print(f"8- Voltar")
    try:
        escolha = int(input("Selecione sua opção: "))
    except ValueError:
        print("Entrada inválida! \nÉ aceito apenas números inteiros.")
    else:
        if escolha == 8:
            return
        if 1<= escolha <= len(funcoes):
            _menuFuncoes(funcoes[escolha - 1])
        else:
            print(f"Erro: Opção inválida! \nPor Gentileza escolha um número entre 1 e {len(funcoes)}, ou 8 para sair." )

# ----- Método para Ver Funções Favoritas ----- #

def _verFavoritos():
    print("--------------------------------------------------")
    
    for opcoes in funcoesFavoritas:
        print(f"{funcoesFavoritas.index(opcoes) + 1}- {opcoes[0]}")
    print(f"8- Voltar")
    try:
        escolha = int(input("Selecione sua opção: "))
    except ValueError:
        print("Entrada inválida! \nÉ aceito apenas números inteiros.")
    else:    
        if len(funcoesFavoritas) == 0:
            print("Não há Funções Favoritadas.")

        if escolha == 8:
            return

# ----- Método para ver Funções na UI ----- #

def _verFuncoesUI():
    print("--------------------------------------------------")
    print("Selecione a opção na UI que deseja alterar: ")

    for opcoes in funcoesUI:
        print(f"{funcoesUI.index(opcoes) + 1}- {opcoes[0]}")
    print(f"8- Voltar")
    try:
        escolha = int(input("Selecione sua opção: "))
    except ValueError:
        print("Entrada inválida! \nÉ aceito apenas números inteiros.")
    else:
        if escolha == 8:
            return        
        if 1<= escolha <= len(funcoes):
             _alterarFuncao(funcoes[escolha - 1])
        else:
            print(f"Erro: Opção inválida! \nPor Gentileza escolha um número entre 1 e {len(funcoes)}, ou 8 para sair." )

# ----- Método de Encerramento do Programa ----- #

def _encerrar():
    print("--------------------------------------------------")
    print("Encerrando...")
    global rodando
    rodando = False

# ----- Método para Tirar Foto ----- #

def _tirarFoto():
    global funcaoAtual

    if funcaoAtual['nome'] != "Vídeo":
        print(f"Foto tirada utilizando a função {funcaoAtual['nome']}")
    else:
        print(f"Vídeo gravado.")

# ----- Lógica do Programa ----- #

while rodando:
    print("--------------------------------------------------")
    escolhaMenu = _menu()


    match escolhaMenu:
        case 1:
            _verFuncoes()
        case 2:
            _tirarFoto()
        case 3:
            _verFuncoesUI()
        case 4:
            _verFavoritos()
        case 5:
            print("--------------------------------------------------")
            print(funcaoAtual['descricao'])
            escolha = input("8- Voltar \nSelecione sua opção: ")
        case 0:
            _encerrar()
        case _:
            print("Insira um valor válido.")