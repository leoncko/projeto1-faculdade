from enum import Enum

def main():
    print("Sistema de inventário")
    while(True):
        menu()
        acao = input("\nEscolha uma ação:")
        if not acao.strip():
            print("Erro! Escolha uma das opções acima!")
            continue
        match acao:
            case '1':
                print("")
            case '2':
                print("")
            case '3':
                print("")
            case '4':
                print("")
            case '5':
                print("")
            case '6':
                print("")
            case '0':
                print("\nEncerrado sistema...")
                break
            case _:
                print("Opção invalida! Digite um número entre 0 e 6.")

class tipoativo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE_LICENCIADO = 4
    BANDCO_DE_DADOS = 5

inventario = {}

def menu():
    print("\nMenu de ações:")
    print("1- Cadastrar novo ativo de TI")
    print("2- Consultar ativo")
    print("3- Atualizar ativo")
    print("4- Apagar ativo")
    print("5- Cadastrar vulnerabilidade no ativo")
    print("6- Consultar vunerabilidades de um ativo")
    print("0- Encerrar o programa")

if __name__ == "__main__":
    main()