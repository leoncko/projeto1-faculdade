import json
from enum import Enum

ARQ_DADOS = "inventario.json"

class tipoativo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE_LICENCIADO = 4
    BANCO_DE_DADOS = 5

class Equipamento:
    def __init__(self, id_equipamento, nome, responsavel, setor):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.responsavel = responsavel
        self.setor = setor
        self.vulnerabilidades = [] 

    def adicionar_vulnerabilidade(self, descricao, gravidade):
        self.vulnerabilidades.append({
            "descricao": descricao, 
            "gravidade": gravidade
        })

    def to_dict(self):
        return {
            "id_equipamento": self.id_equipamento,
            "nome": self.nome,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "tipo": self.__class__.__name__, 
            "vulnerabilidades": self.vulnerabilidades
        }

class Notebook(Equipamento):
    pass
class Servidor(Equipamento):
    pass
class Roteador(Equipamento):
    pass
class SoftwareLicenciado(Equipamento):
    pass
class BancoDeDados(Equipamento):
    pass


def carregar_dados():
    try:
        with open(ARQ_DADOS, "r") as f:
            lista_dados = json.load(f)
            inventario_recuperado = {}
            
            for item in lista_dados:
                id_ativo = item["id_equipamento"]
                nome = item["nome"]
                responsavel = item["responsavel"]
                setor = item["setor"]
                tipo_str = item["tipo"]

                if tipo_str == "Notebook":
                    obj = Notebook(id_ativo, nome, responsavel, setor)
                elif tipo_str == "Servidor":
                    obj = Servidor(id_ativo, nome, responsavel, setor)
                elif tipo_str == "Roteador":
                    obj = Roteador(id_ativo, nome, responsavel, setor)
                elif tipo_str == "SoftwareLicenciado":
                    obj = SoftwareLicenciado(id_ativo, nome, responsavel, setor)
                elif tipo_str == "BancoDeDados":
                    obj = BancoDeDados(id_ativo, nome, responsavel, setor)
                else:
                    obj = Equipamento(id_ativo, nome, responsavel, setor)

                obj.vulnerabilidades = item.get("vulnerabilidades", [])
                inventario_recuperado[id_ativo] = obj

            return inventario_recuperado
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_dados(inventario):
    lista_json = [ativo.to_dict() for ativo in inventario.values()]
    with open(ARQ_DADOS, "w") as f:
        json.dump(lista_json, f, indent=4)