import input, validator, storage, calculation

indice_lista: int = 0
total_adicao: int = 0
total_multiplicacao: int = 1
numeros_inteiros: list[int] = []
numeros_duplicados: list[int] = []
numeros_impares: list[int] = []
numeros_pares: list[int] = []
numeros_primos: list[int] = []


def executar_rotina_entrada(lista: list[int]):
    entrada: str = input.ler_entrada()
    numero: int = validator.validar_entrada(entrada)
    match numero:
        case 0:
            print(f"\n\n\tLista de números inteiros: {lista}")
        case None:
            executar_rotina_entrada(lista)
        case _:
            storage.armazenar_entrada(numero, lista)
            executar_rotina_entrada(lista)

def executar_rotina_calculo(lista: list[int], indice: int, adicao: int, multiplicacao: int):
    iterar_adicao(lista, indice, adicao)
    iterar_multiplicacao(lista, indice, multiplicacao)

def iterar_adicao(lista: list[int], indice: int, total: int):
    total = calculation.obter_adicao(lista, indice, total)
    if indice != lista.index(lista[-1]):
        indice += 1
        iterar_adicao(lista, indice, total)
    else:
        print(f"\tTotal sobre adição: {total}")

def iterar_multiplicacao(lista: list[int], indice: int, total: int):
    total = calculation.obter_multiplicacao(lista, indice, total)
    if indice != lista.index(lista[-1]):
        indice += 1
        iterar_multiplicacao(lista, indice, total)
    else:
        print(f"\tTotal sobre multiplicação: {total}")

executar_rotina_entrada(numeros_inteiros)
executar_rotina_calculo(numeros_inteiros, indice_lista, total_adicao, total_multiplicacao)