# ----- Variáveis globais ----- #
rodando = True
funcaoAtual = ""

# ----- Definição de Funções ----- #
funcoes = []
funcoesFavoritas = []

    #Método que cria funções da câmera com nome e descrição e as adiciona à lista de funções.
def _criarFuncao(nome, descricao):
    funcao = [nome, descricao]
    funcoes.append(funcao)

_criarFuncao("Automática", "Função padrão de foto.")
_criarFuncao("Vídeo", "Segure o botão vermelho para iniciar a gravação.")
_criarFuncao("Panorâmica", "Segure o botão de foto e mova o celular para criar uma foto esticada.")
_criarFuncao("Ler Texto", "Aponte a câmera para qualquer texto e aperte o botão. O texto será transcrito digitalmente.")

funcoesUI = [funcoes[0], funcoes[1]]

# ----- Método para Alterar Função ----- #

funcaoAtual = funcoes[0]

def _alterarFuncao(funcao):
    global funcaoAtual
    funcaoAtual = funcao
    print(f"Alterando para a função {funcao[0]}")
   

# ----- Método para Favoritar Função ----- #

def _favoritarFuncao(funcao):
    global funcoesFavoritas
    funcoesFavoritas = funcoesFavoritas
    
    i = 0

    if funcao[0] == funcoesUI[0][0] or funcao[0] == funcoesUI[1][0]:
        print("Essa função é uma função padrão.")
        return

    if len(funcoesFavoritas) > 0:
        for func in funcoesFavoritas:

            if func[0] == funcao[0]:
                escolha = int(input("Função já favoritada. Deseja remover dos Favoritos? \n1- Sim \n2- Não \nSelecione sua opção: "))

                if escolha == 1:
                    funcoesFavoritas.pop(i)
                    funcoesUI.pop(i + 2)
            elif i == (len(funcoesFavoritas) - 1) and func[0] != funcao[0]:
                funcoesFavoritas.append(funcao)
                funcoesUI.append(funcao)
                print(f"Favoritando a função {funcao[0]}")
                break;
            i += 1
    else:
        funcoesFavoritas.append(funcao)
        funcoesUI.append(funcao)
        print(f"Favoritando a função {funcao[0]}")

# ----- Método do Menu Inicial ----- #

def _menu():
    print("O que deseja fazer?")
    print(f"1- Ver Funções \n2- Tirar Foto \n3- Alterar entre funções na UI \n4- Ver Favoritos \n5- Ver Descrição da Função Atual \n0- Encerrar Programa")
    escolha = int(input("Selecione sua opção: "))
    return escolha

# ----- Método do Menu de Funções ----- #

def _menuFuncoes(funcao):
    print("--------------------------------------------------")
    print("O que deseja fazer em relação à função?")
    print(f"1- Alterar para a Função \n2- Favoritar a Função \n3- Favoritar e Alterar para a Função \n4- Ler Descrição da Função \n8- Voltar \n9- Voltar ao Menu Inicial")
    escolha = int(input("Selecione sua opção: "))

    match escolha:
        case 1:
            _alterarFuncao(funcao)
        case 2:
            _favoritarFuncao(funcao)
        case 3:
            _alterarFuncao(funcao)
            _favoritarFuncao(funcao)
        case 4:
            print(funcao[1])
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
        print(f"{funcoes.index(opcoes) + 1}- {opcoes[0]}")
    print(f"8- Voltar")
    escolha = int(input("Selecione sua opção: "))

    if escolha == 8:
        return
    print(f"função: {funcoes[escolha - 1]}")
    _menuFuncoes(funcoes[escolha - 1])

# ----- Método para Ver Funções Favoritas ----- #

def _verFavoritos():
    print("--------------------------------------------------")
    
    for opcoes in funcoesFavoritas:
        print(f"{funcoesFavoritas.index(opcoes) + 1}- {opcoes[0]}")
    print(f"8- Voltar")
    escolha = int(input("Selecione sua opção: "))

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
    escolha = int(input("Selecione sua opção: "))

    if escolha == 8:
        return
    _alterarFuncao(funcoesUI[escolha - 1])

# ----- Método de Encerramento do Programa ----- #

def _encerrar():
    print("--------------------------------------------------")
    print("Encerrando...")
    global rodando
    rodando = False

# ----- Método para Tirar Foto ----- #

def _tirarFoto():
    global funcaoAtual

    if funcaoAtual[0] != "Vídeo":
        print(f"Foto tirada utilizando a função {funcaoAtual[0]}")
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
            print(funcaoAtual[1])
            escolha = input("8- Voltar \nSelecione sua opção: ")
        case 0:
            _encerrar()
        case _:
            print("Insira um valor válido.")