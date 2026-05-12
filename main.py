import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import math
from matplotlib.lines import Line2D

# Criando o grafo
grafo = nx.Graph()

# Lista de locais da UFMA
locais = [
    "Portão Principal",
    "Parada de Ônibus",
    "CCET",
    "Biblioteca Central",
    "Restaurante Universitário",
    "Reitoria",
    "Centro Pedagógico Paulo Freire",
    "CCH",
    "CCSO",
    "NTI"
]
coordenadas = {
    "Portão Principal": (0, 3),
    "Parada de Ônibus": (2, 3),
    "CCET": (4, 4),
    "Biblioteca Central": (6, 5),
    "Restaurante Universitário": (7, 3),
    "Reitoria": (6, 2),
    "Centro Pedagógico Paulo Freire": (3, 1),
    "CCH": (5, 0),
    "CCSO": (7, 1),
    "NTI": (5, 2)
}

# Adicionando os nós
grafo.add_nodes_from(locais)

# Conexões com distância, condição e penalidade

conexoes = [
    {
        "origem": "Portão Principal",
        "destino": "Parada de Ônibus",
        "distancia": 120,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "Parada de Ônibus",
        "destino": "CCET",
        "distancia": 200,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "Parada de Ônibus",
        "destino": "Centro Pedagógico Paulo Freire",
        "distancia": 260,
        "condicao": "Piso irregular",
        "penalidade": 80
    },

    {
        "origem": "CCET",
        "destino": "Biblioteca Central",
        "distancia": 300,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "CCET",
        "destino": "Reitoria",
        "distancia": 250,
        "condicao": "Escada",
        "penalidade": 500
    },

    {
        "origem": "CCET",
        "destino": "NTI",
        "distancia": 180,
        "condicao": "Caminho estreito",
        "penalidade": 180
    },

    {
        "origem": "Biblioteca Central",
        "destino": "Restaurante Universitário",
        "distancia": 180,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "Biblioteca Central",
        "destino": "Reitoria",
        "distancia": 220,
        "condicao": "Rampa inclinada",
        "penalidade": 150
    },

    {
        "origem": "Restaurante Universitário",
        "destino": "CCSO",
        "distancia": 260,
        "condicao": "Baixa iluminação",
        "penalidade": 100
    },

    {
        "origem": "Reitoria",
        "destino": "CCSO",
        "distancia": 210,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "Centro Pedagógico Paulo Freire",
        "destino": "CCH",
        "distancia": 280,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "CCH",
        "destino": "CCSO",
        "distancia": 240,
        "condicao": "Piso irregular",
        "penalidade": 80
    },

    {
        "origem": "CCSO",
        "destino": "NTI",
        "distancia": 300,
        "condicao": "Acessível",
        "penalidade": 0
    },

    {
        "origem": "NTI",
        "destino": "Reitoria",
        "distancia": 190,
        "condicao": "Acessível",
        "penalidade": 0
    }
]

# Inserindo arestas no grafo
for conexao in conexoes:

    peso_final = (
        conexao["distancia"] +
        conexao["penalidade"]
    )

    grafo.add_edge(
        conexao["origem"],
        conexao["destino"],
        weight=peso_final,
        distancia=conexao["distancia"],
        condicao=conexao["condicao"],
        penalidade=conexao["penalidade"]
    )

# Definindo origem e destino
print("\n===== LOCAIS DISPONÍVEIS =====")

for indice, local in enumerate(locais, start=1):
    print(f"{indice}. {local}")

origem_indice = int(input("\nDigite o número do local de origem: "))
destino_indice = int(input("Digite o número do local de destino: "))

origem = locais[origem_indice - 1]
destino = locais[destino_indice - 1]

def heuristica(no_atual, destino):
    x1, y1 = coordenadas[no_atual]
    x2, y2 = coordenadas[destino]

    distancia_reta = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distancia_reta * 100

# Aplicando algoritmo A*
caminho = nx.astar_path(
    grafo,
    origem,
    destino,
    heuristic=heuristica,
    weight="weight"
)

# Calculando custo total
custo_total = nx.astar_path_length(
    grafo,
    origem,
    destino,
    heuristic=heuristica,
    weight="weight"
)

# Exibindo resultado
print("\n" + "=" * 50)
print("RESULTADO DA BUSCA")
print("=" * 50)
print(f"Origem: {origem}")
print(f"Destino: {destino}")

print("\nMelhor rota encontrada:")
print(" -> ".join(caminho))

print(f"\nCusto total da rota: {custo_total}")

print("\n" + "=" * 50)
print("DETALHES DA ROTA")
print("=" * 50)
custo_acumulado = 0
for i in range(len(caminho) - 1):

    origem_atual = caminho[i]
    destino_atual = caminho[i + 1]

    dados = grafo[origem_atual][destino_atual]

custo_acumulado += dados['weight']

print(f"""
Trecho:
{origem_atual} -> {destino_atual}

Distância: {dados['distancia']} metros
Condição: {dados['condicao']}
Penalidade: {dados['penalidade']}
Peso final: {dados['weight']}

Custo acumulado da rota: {custo_acumulado}
""")
# Análise final da rota

print("\n" + "=" * 50)
print("ANÁLISE DA ROTA")
print("=" * 50)

if custo_total <= 500:
    print("A rota encontrada possui alta acessibilidade.")

elif custo_total <= 900:
    print("A rota encontrada possui acessibilidade moderada.")

else:
    print("A rota encontrada apresenta dificuldades de acessibilidade.")

# Verificando obstáculos

obstaculos = []

for i in range(len(caminho) - 1):

    origem_atual = caminho[i]
    destino_atual = caminho[i + 1]

    dados = grafo[origem_atual][destino_atual]

    if dados["condicao"] != "Acessível":
        obstaculos.append(dados["condicao"])

if obstaculos:

    print("\nPossíveis obstáculos encontrados:")

    for obstaculo in set(obstaculos):
        print(f"- {obstaculo}")

else:
    print("\nNenhum obstáculo significativo encontrado.")
# Criando posição visual dos nós
pos = coordenadas

# Tamanho da janela
plt.figure(figsize=(14, 9))

# Desenhando nós e conexões
nx.draw_networkx_nodes(
    grafo,
    pos,
    node_color="lightblue",
    node_size=3000
)

nx.draw_networkx_labels(
    grafo,
    pos,
    font_size=8,
    font_weight="bold"
)

# Definindo cores das conexões baseado na acessibilidade

cores_arestas = []

for u, v, dados in grafo.edges(data=True):

    condicao = dados["condicao"]

    if condicao == "Acessível":
        cores_arestas.append("green")

    elif condicao == "Escada":
        cores_arestas.append("red")

    else:
        cores_arestas.append("orange")

# Desenhando conexões
nx.draw_networkx_edges(
    grafo,
    pos,
    edge_color=cores_arestas,
    width=2
)

# Mostrar pesos nas arestas
pesos = nx.get_edge_attributes(grafo, "weight")

nx.draw_networkx_edge_labels(
    grafo,
    pos,
    edge_labels=pesos,
    font_size=8
)

# Destacar caminho encontrado
arestas_caminho = list(zip(caminho, caminho[1:]))

nx.draw_networkx_edges(
    grafo,
    pos,
    edgelist=arestas_caminho,
    edge_color="blue",
    width=5
)

# Título
plt.title(
    "Sistema Inteligente de Rotas Acessíveis na UFMA usando A*",
    fontsize=16,
    fontweight="bold"
)
# Criando legenda personalizada

legenda = [

    Line2D(
        [0],
        [0],
        color="green",
        lw=3,
        label="Caminho acessível"
    ),

    Line2D(
        [0],
        [0],
        color="orange",
        lw=3,
        label="Acessibilidade moderada"
    ),

    Line2D(
        [0],
        [0],
        color="red",
        lw=3,
        label="Caminho com escada"
    ),

    Line2D(
        [0],
        [0],
        color="blue",
        lw=4,
        label="Melhor rota encontrada"
    )
]

plt.legend(
    handles=legenda,
    loc="upper left"
)

# Mostrar gráfico
plt.savefig(
    "grafo_rota_acessivel.png",
    dpi=300,
    bbox_inches="tight"
)