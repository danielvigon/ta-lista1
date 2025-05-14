def obter_adicao(lista: list[int], indice: int = 0, adicao: int = 0) -> int:
    return adicao if indice == len(lista) else obter_adicao(lista, indice + 1, adicao + lista[indice])

def obter_multiplicacao(lista: list[int], indice: int = 0, multiplicacao: int = 1) -> int:
    return multiplicacao if indice == len(lista) else obter_multiplicacao(lista, indice + 1, multiplicacao * lista[indice])

def obter_duplicados(lista: list[int], indice: int = 0, duplicados: list[list[int]] = [[],[]]) -> list[int]:
    if indice == len(lista):
        duplicados[1].sort()
        return duplicados[1]
    elif duplicados[0] == []:
            duplicados[0] = lista.copy()
    else:
        duplicados[0].remove(lista[indice])
        if lista[indice] in duplicados[0] and lista[indice] not in duplicados[1]:
            duplicados[1].append(lista[indice])
    return obter_duplicados(lista, indice + 1, duplicados)

def obter_impares(lista: list[int], impares: set[int] = set(), indice: int = 0) -> list[int]:
    if indice == len(lista):
        return list(impares)
    elif lista[indice] // 2 != lista[indice] / 2:
        impares.add(lista[indice])
    return obter_impares(lista, impares, indice + 1)

def obter_pares(lista: list[int], pares: set[int] = set(), indice: int = 0) -> list[int]:
    if indice == len(lista):
        return list(pares)
    elif lista[indice] // 2 == lista[indice] / 2:
        pares.add(lista[indice])
    return obter_pares(lista, pares, indice + 1)

def obter_primos(lista: list[int], primos: set[int] = set(), indice: int = 0, crivo: dict[int, list[int]] = {2:[]}) -> list[int]:
    if indice == len(lista):
        return list(primos)
    elif crivo == {}:
        crivo = int(max(lista)**0.5)
    elif lista[indice] > 1 and lista[indice] // crivo != lista[indice] / crivo and lista[indice] % range(2, crivo) != 0:
        primos.add(lista[indice])
        obter_primos(lista, primos, indice, crivo -1)
    return obter_primos(lista, primos, indice +1, crivo)

        






