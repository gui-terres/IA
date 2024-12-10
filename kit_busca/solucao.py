from typing import Iterable, Set, Tuple
import solucao as solucao
import heapq

class Nodo:
    def __init__(self, estado, pai=None, acao=None, custo=0, heuristica=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.heuristica = heuristica
        self.f = custo + heuristica  

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __eq__(self, other):
        return self.f == other.f
    
    def __hash__(self):
        return hash(self.estado)

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    movimentos = {
        "esquerda": -1,
        "direita": 1,
        "acima": -3,
        "abaixo": 3,
    }

    resultados = set()

    posicao_vazia = estado.index('_')

    for acao, deslocamento in movimentos.items():
        nova_posicao = posicao_vazia + deslocamento

        if (
            0 <= nova_posicao < 9  
            and not (posicao_vazia % 3 == 0 and acao == "esquerda")  
            and not (posicao_vazia % 3 == 2 and acao == "direita")   
        ):
            estado_lista = list(estado)
            estado_lista[posicao_vazia], estado_lista[nova_posicao] = (
                estado_lista[nova_posicao],
                estado_lista[posicao_vazia],
            )
            novo_estado = "".join(estado_lista)
            
            resultados.add((acao, novo_estado))

    return resultados


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    sucessores = sucessor(nodo.estado)
    
    nodos_sucessores = set()

    for acao, estado_sucessor in sucessores:
        novo_nodo = Nodo(
            estado=estado_sucessor,
            pai=nodo,
            acao=acao,
            custo=nodo.custo + 1
        )
        nodos_sucessores.add(novo_nodo)  

    return nodos_sucessores


def hamming(estado: str) -> int:
    """
    Calcula a distância de Hamming, ou seja, o número de peças fora de lugar.
    """

    objetivo = "12345678_"  #objetivo
    return sum(1 for a, b in zip(estado, objetivo) if a != b and a != '_')


def manhattan(estado: str) -> int:
    """
    Calcula a soma das distâncias de Manhattan de todas as peças do estado.
    A distância Manhattan é a soma das distâncias verticais e horizontais
    de cada peça até a posição correta.
    """

    objetivo = "12345678_"
    distancia = 0
    for i, char in enumerate(estado):
        if char != '_':
            objetivo_pos = objetivo.index(char)
            distancia += abs(i // 3 - objetivo_pos // 3) + abs(i % 3 - objetivo_pos % 3)
    return distancia


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = "12345678_"
    
    if estado == objetivo:
        return [] 
    
    fronteira = []
    explorados = set()
    
    raiz = Nodo(estado, None, None, 0)  
    heapq.heappush(fronteira, (hamming(estado), raiz))  
    
    while fronteira:
        _, nodo_atual = heapq.heappop(fronteira)
        
        if nodo_atual.estado in explorados:
            continue
        explorados.add(nodo_atual.estado)
        
        if nodo_atual.estado == objetivo:
            caminho = []
            while nodo_atual.pai:
                caminho.append(nodo_atual.acao)
                nodo_atual = nodo_atual.pai
            return caminho[::-1]  
        
        for acao, estado_sucessor in sucessor(nodo_atual.estado):
            if estado_sucessor not in explorados:
                custo = nodo_atual.custo + 1  
                nodo_sucessor = Nodo(estado_sucessor, nodo_atual, acao, custo)
                f = custo + hamming(estado_sucessor)  
                heapq.heappush(fronteira, (f, nodo_sucessor))  
    return None  


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = "12345678_"
    
    if estado == objetivo:
        return []  
    
    fronteira = []
    explorados = set()
    
    raiz = Nodo(estado, None, None, 0)  
    heapq.heappush(fronteira, (manhattan(estado), raiz))  
    
    while fronteira:
        _, nodo_atual = heapq.heappop(fronteira)
        
        if nodo_atual.estado in explorados:
            continue
        explorados.add(nodo_atual.estado)
        
        if nodo_atual.estado == objetivo:
            caminho = []
            while nodo_atual.pai:
                caminho.append(nodo_atual.acao)
                nodo_atual = nodo_atual.pai
            return caminho[::-1]  
        
        for acao, estado_sucessor in sucessor(nodo_atual.estado):
            if estado_sucessor not in explorados:
                custo = nodo_atual.custo + 1  
                nodo_sucessor = Nodo(estado_sucessor, nodo_atual, acao, custo)
                f = custo + manhattan(estado_sucessor)  
                heapq.heappush(fronteira, (f, nodo_sucessor))  
    return None  

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
