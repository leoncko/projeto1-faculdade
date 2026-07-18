from dados import carregar_dados
from funcoes import cadastro, atualizar, deletar, cadastrar_vul

def main():

    inventario = carregar_dados()

    print("Sistema de inventário")
    while(True):
        menu()
        acao = input("\nEscolha uma ação:")
        if not acao.strip():
            print("Erro! Escolha uma das opções acima!")
            continue
        match acao:
            case '1':
                cadastro(inventario)
            case '2':
                consulta(inventario)
            case '3':
                atualizar(inventario)
            case '4':
                deletar(inventario)
            case '5':
                cadastrar_vul(inventario)
            case '6':
                consultar_vul(inventario)
            case '0':
                print("\nEncerrado sistema...")
                break
            case _:
                print("Opção invalida! Digite um número entre 0 e 6.")

def menu():
    print("\nMenu de ações:")
    print("1- Cadastrar novo ativo de TI")
    print("2- Consultar ativo")
    print("3- Atualizar ativo")
    print("4- Apagar ativo")
    print("5- Cadastrar vulnerabilidade no ativo")
    print("6- Consultar vunerabilidades de um ativo")
    print("0- Encerrar o programa")

def consulta(inventario):
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

def consultar_vul(inventario):
    print("\nConsulta de vulnerabilidades:")

    if not inventario:
        print("Não há como consultar pois o inventário está vazio!")
        return

    try:
        id_busca = int(input("Digite o ID do ativo para ver suas vulnerabilidades: "))
    except ValueError:
        print("Erro: O ID é um número inteiro.")
        return

    if id_busca in inventario:
        ativo = inventario[id_busca]
        print(f"\nVulnerabilidades do Ativo: {ativo['nome']}")
        
        lista_vul = ativo['vulnerabilidades']
        
        if len(lista_vul) == 0:
            print("Nenhuma vulnerabilidade registrada nesse ativo!")
        else:
            for id, vul in enumerate(lista_vul, start=1):
                print(f"{id}. Descrição: {vul['descricao']} | Gravidade: {vul['gravidade']}")
    else:
        print(f"Erro! Ativo com ID {id_busca} não encontrado.")

if __name__ == "__main__":
    main()