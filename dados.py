from enum import Enum
import json

ARQ_DADOS = "inventario.txt"

class tipoativo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE_LICENCIADO = 4
    BANCO_DE_DADOS = 5

def carregar_dados():
    try:
        with open(ARQ_DADOS, "r") as f:
            dados = json.load(f)
            inventario2 = {}
            for id_texto, dados_ativo in dados.items():
                inventario2[int(id_texto)] = dados_ativo
            return inventario2
    except FileNotFoundError:
        return {}


def salvar_dados(inventario):
    with open(ARQ_DADOS, "w") as f:
        json.dump(inventario, f, indent=4)
