from input import ler_entrada
from validator import validar_entrada
from storage import armazenar_entrada


numeros_inteiros: list[int] = []


def executar_rotina_entrada(lista: list[int]):
    entrada:str = ler_entrada()
    numero:int = validar_entrada(entrada)
    match numero:
        case 0:
            exibir_listas(lista)
        case None:
            executar_rotina_entrada(lista)
        case _:
            armazenar_entrada(numero, lista)
            executar_rotina_entrada(lista)

def exibir_listas(inteiros: list[int],):
    print(f"\n\n\tLista de números inteiros: {inteiros}")

executar_rotina_entrada(numeros_inteiros)