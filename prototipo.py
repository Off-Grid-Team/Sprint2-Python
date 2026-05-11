print("\nAplicativo de Câmera")
print("---------------------------------------------------")

rodando = True
funcoes = ["automática", "vídeo", "panorâmica", "etc1", "etc2", "etc3"]
funcoesUI = ["automática", "vídeo"]
funcoesFavoritas = []

funcaoAtual = funcoes[0]

def _escolherFuncao():
    print("Selecione a função que deseja ver: ")

    for opcoes in funcoes:
        print(f"{funcoes.index(opcoes) + 1}- {opcoes}")
    print("0- Voltar")

    escolhaFuncoes = int(input())
    
    print("---------------------------------------------------")
    
    match escolhaFuncoes:
        case 1:
            print("Função padrão de foto")
        case 2:
            print("Função padrão de vídeo")
        case 0:
            print("Voltando")
            print("---------------------------------------------------")
    print("O que deseja fazer em relação a função?")

    funcaoEscolhida = funcoes[escolhaFuncoes - 1]

    fav = _checarFavorito(funcaoEscolhida)

    opcoesFuncoes = int(input("1- Favoritar Função \n2- Alterar função \n3- Favoritar e alterar para função \n4- Informação \n0- Voltar \n\n"))
    
    print("\n")

    match opcoesFuncoes:
        case 1:
            if fav != True:
                funcoesFavoritas.append(funcaoEscolhida)
                print(f"Favoritou a função {funcoesFavoritas[0]}")
            else:
                print("Função já favoritada, deseja desfavoritar?")
                desfav = int(input("1- Sim \n2- Não \n"))

                if desfav == 1:
                    funcoesFavoritas.pop(funcoesFavoritas.index(funcaoEscolhida))
                    print(f"Removeu a função {funcaoEscolhida} dos Favoritos.")
                else:
                    print("Voltando")

        case 2:
            _alterarFuncao(funcaoEscolhida)
            print(f"Alterou para a função {funcaoAtual}")
        case 3:
            if fav != True:
                funcoesFavoritas.append(funcaoEscolhida)
                print(f"Favoritou a função {funcoesFavoritas[0]}")
            else:
                print("Função já favoritada, deseja desfavoritar?")
                desfav = int(input("1- Sim \n2- Não\n"))

                if desfav == 1:
                    funcoesFavoritas.pop(funcoesFavoritas.index(funcaoEscolhida))
                    print(f"Removeu a função {funcaoEscolhida} dos Favoritos.")
                else:
                    print("Continuando")

            _alterarFuncao(funcaoEscolhida)
            print(f"Alterou para a função {funcaoAtual}")
        case 4:
            print(_info(funcaoAtual))
        case 0:
            print("Voltando")
    print("---------------------------------------------------")

def _escolherFuncaoUI():
    print("Qual modo deseja selecionar?")

    for opcoesUI in funcoesUI:
        print(f"Função {funcoesUI.index(opcoesUI) + 1}: {opcoesUI}")

    escolhaFuncoesUI = int(input())
    match escolhaFuncoesUI:
        case 1:
            _alterarFuncao(funcoesUI[escolhaFuncoesUI - 1])
            print(f"Alternado para função {funcaoAtual}")
        case 2:
            _alterarFuncao(funcoesUI[escolhaFuncoesUI - 1])
            print(f"Alternado para função {funcaoAtual}")
        case 3:
            if escolhaFuncoesUI >= len(funcoesUI):
               _alterarFuncao(funcoesUI[escolhaFuncoesUI - 1])
               print(f"Alternado para função {funcaoAtual}")
        case 4:
            if escolhaFuncoesUI >= len(funcoesUI):
                _alterarFuncao(funcoesUI[escolhaFuncoesUI - 1])
                print(f"Alternado para função {funcaoAtual}")
        case 5:
            if escolhaFuncoesUI >= len(funcoesUI):
                _alterarFuncao(funcoesUI[escolhaFuncoesUI - 1])
                print(f"Alternado para função {funcaoAtual}")

def _checarFavorito(funcao):
    for fav in funcoesFavoritas:
        if funcao == fav:
            return True
            break
        else:
            return False
        
def _alterarFuncao(funcao):
    global funcaoAtual
    funcaoAtual = funcao

def _info(funcao):
    print(f"informação da função {funcao}")

while rodando:
    print("O que deseja fazer?") 
    escolha = int(input("1- Ver funções \n2- Tirar foto \n3- Alterar entre funções na UI \n4- Ver Favoritos \n5- Informações da função atual \n9- Encerrar Programa \n\n"))

    print("---------------------------------------------------")

    match escolha:
        case 1:
            _escolherFuncao()
        case 2:
            if (funcaoAtual != "vídeo"):
                print(f"Foto tirada no modo {funcaoAtual}")
            else:
                print(f"Vídeo gravado.")
        case 3:
            _escolherFuncaoUI()
        case 4:
            print("Funcões Favoritas:\n")
            if len(funcoesFavoritas) != 0:
                for fav in funcoesFavoritas:
                    i = 1
                    print(f"{i}- {fav}")
                    i += 1
            else:
                print("Não há funções favoritas.")
        case 5:
            print(_info(funcaoAtual))
        case 9:
            print("Encerrando...")
            rodando = False
    print("---------------------------------------------------")