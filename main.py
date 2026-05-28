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
                cadastro()
            case '2':
                consulta()
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


def cadastro():
    print("\nNovo cadastro:")

    while True:
        try:
            id_ativo = int(input("\nDigite o ID do novo ativo a cadastrar:"))
            if id_ativo <= 0:
                print("\nErro!\nO ID não pode ser um número negativo!")
                continue
            if id_ativo in inventario:
                print("\nErro!\nEsse ID já existe no sistema!")
                continue
            break
        except ValueError:
            print("\nErro!\nO ID deve ser um número inteiro!")

    nome = input("\nDigite o nome ou hostname do ativo:").strip()
    responsavel = input("\nQual o nome do responsável pelo ativo?").strip()
    setor = input("\nEm que setor ou localização o ativo será cadastrado:").strip()

    print("\nCategorias de ativos do sistema:")
    for tipo in tipoativo:
        print(f"{tipo.value}- {tipo.name}")

    while True:
        try:
            escolha_tipo = int(input("\nDigite o número da categoria selecionada:"))
            tipo_escolhido = tipoativo(escolha_tipo)
            break
        except ValueError:
            print("\nErro!\nDigite um dos valores da lista!")

    inventario[id_ativo] = {
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo_escolhido.name,
        "vulnerabilidades": []
    }

    print(f"\nAtivo {nome} com ID: {id_ativo} - cadastrado com sucesso!")


def consulta():
    print("\nConsulta de ativo:")

    if not inventario:
        print("\nNão há ativos cadastrados ainda... Cadastre um ativo primeiro!")
        return
    
    termo = input("Digite o ID ou nome do ativo que deseja consultar:").strip()
    ativo_encontrado = None
    id_encontrado = None

    if termo.isdigit():
        id_busca = int(termo)
        if id_busca in inventario:
            ativo_encontrado = inventario[id_busca]
            id_encontrado = id_busca
    
    if not ativo_encontrado:
        for id_ativo, dados in inventario.items():
            if dados['nome'].lower() == termo.lower():
                ativo_encontrado = dados
                id_encontrado = id_ativo
                break
    
    if ativo_encontrado:
        print(f"ID: {id_encontrado}")
        print(f"Nome/Hostname: {ativo_encontrado['nome']}")
        print(f"Responsável: {ativo_encontrado['responsavel']}")
        print(f"Setor/Loc: {ativo_encontrado['setor']}")
        print(f"Tipo: {ativo_encontrado['tipo']}")

        qnt_vuln = len(ativo_encontrado['vulnerabilidades'])
        print(f"Vulnerabilidades: {qnt_vuln}")

    else:
        print(f"Nenhum ativo encontrado pela busca {termo}")


if __name__ == "__main__":
    main()