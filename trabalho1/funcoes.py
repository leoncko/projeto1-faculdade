from dados import tipoativo, salvar_dados, Notebook, Servidor, Roteador, SoftwareLicenciado, BancoDeDados

def cadastro(inventario):
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

    if tipo_escolhido == tipoativo.NOTEBOOK:
        novo_ativo = Notebook(id_ativo, nome, responsavel, setor)
    elif tipo_escolhido == tipoativo.SERVIDOR:
        novo_ativo = Servidor(id_ativo, nome, responsavel, setor)
    elif tipo_escolhido == tipoativo.ROTEADOR:
        novo_ativo = Roteador(id_ativo, nome, responsavel, setor)
    elif tipo_escolhido == tipoativo.SOFTWARE_LICENCIADO:
        novo_ativo = SoftwareLicenciado(id_ativo, nome, responsavel, setor)
    elif tipo_escolhido == tipoativo.BANCO_DE_DADOS:
        novo_ativo = BancoDeDados(id_ativo, nome, responsavel, setor)

    inventario[id_ativo] = novo_ativo

    print(f"\nAtivo {nome} com ID: {id_ativo} - cadastrado com sucesso!")
    salvar_dados(inventario)

def atualizar(inventario):
    print("\nAtualização de ativos")

    if not inventario:
        print("\nO inventário está vazio!")
        return
        
    try:
        id_busca = int(input("Qual ativo deseja atualizar? ID:"))
    except ValueError:
        print("Erro! O ID é sempre um número inteiro.")
        return
        
    if id_busca in inventario:
        ativo = inventario[id_busca]
        print(f"\nAtivo {ativo.nome} encontrado!")
        print("Apenas aperte Enter caso não queira modificar um campo:")
        
        novo_nome = input(f"Nome atual: {ativo.nome} / Novo nome:").strip()
        novo_responsavel = input(f"Responsável atual: {ativo.responsavel} / Novo responsável:").strip()
        novo_setor = input(f"Setor atual: {ativo.setor} / Novo setor:").strip()

        if novo_nome:
            ativo.nome = novo_nome
        if novo_responsavel:
            ativo.responsavel = novo_responsavel
        if novo_setor:
            ativo.setor = novo_setor
            
        print(f"\nAtivo {id_busca} atualizado com sucesso!")
        salvar_dados(inventario)
        
    else:
        print(f"\nErro! Ativo {id_busca} não encontrado.")

def deletar(inventario):
    print("Deletar Ativo:")

    if not inventario:
        print("Não é possível realizar a ação pois o inventário está vazio!")
        return
    
    try:
        id_busca = int(input("Digite o ID do ativo que deseja excluir:"))
    except ValueError:
        print("O ID deve ser um número inteiro positivo!")
        return
    
    if id_busca in inventario:
        ativo = inventario[id_busca]
        while True:
            try:
                confirmar = int(input(f"\nTem certeza que deseja excluir o ativo: {ativo.nome}?\nDigite 1 para confirmar e qualquer outro número para cancelar:"))
                break
            except ValueError:
                print("Digite apenas números, não caracteres!") 
                continue
        if confirmar == 1:
            del inventario[id_busca]
            print(f"Ativo {id_busca} deletado com sucesso!")
            salvar_dados(inventario)
        else:
            print("Exclusão cancelada!")
    else:
        print(f"Erro! Ativo {id_busca} não encontrado!")

def cadastrar_vul(inventario):
    print("\nCadastro de vulnerabilidades:")

    if not inventario:
        print("O inventário está vazio, não é possivel cadastrar!")
        return

    try:
        id_busca = int(input("Digite o ID do ativo vulneravel:"))
    except ValueError:
        print("Erro! O ID é um número inteiro.")
        return

    if id_busca in inventario:
        ativo = inventario[id_busca]
        print(f"\nAtivo selecionado: {ativo.nome}")
        
        descricao = input("Descreva a vulnerabilidade: ").strip()
        if not descricao:
            print("A descrição não pode ficar vazia, processo cancelado!")
            return
        
        gravidade = input("Qual a gravidade? (Baixa/Media/Grave/Extrema): ").strip().upper()
        if gravidade not in ["BAIXA", "MEDIA", "GRAVE", "EXTREMA"]:
            print("Erro! Gravidade inválida ou em branco. Use apenas Baixa, Media, Grave ou Extrema.")
            return
        
        ativo.adicionar_vulnerabilidade(descricao, gravidade)
        
        print(f"\nVulnerabilidade registrada no ativo '{ativo.nome}'.")
        salvar_dados(inventario)
    else:
        print(f"Erro! Ativo com ID {id_busca} não encontrado.")