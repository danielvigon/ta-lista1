def obter_adicao(lista: list[int], indice: int = 0, total: int = 0) -> int:
    return total if indice == len(lista) else obter_adicao(lista, indice + 1, total + lista[indice])

def obter_multiplicacao(lista: list[int], indice: int = 0, total: int = 1) -> int:
    return total if indice == len(lista) else obter_multiplicacao(lista, indice + 1, total * lista[indice])