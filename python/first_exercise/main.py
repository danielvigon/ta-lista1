import input, validator, storage, calculation

entrada: list[int] = []
adicao: list[int] = []
multiplicacao: list[int] = []
duplicados: list[int] = []
impares: list[int] = []
pares: list[int] = []
primos: list[int] = []


def executar_rotina_entrada(lista: list[int]):
    entrada: str = input.ler_entrada()
    numero: int = validator.validar_entrada(entrada)
    if entrada == '0':
            pass
    elif numero == 0:
            executar_rotina_entrada(lista)
    else:
            storage.armazenar_parametro(numero, lista)
            executar_rotina_entrada(lista)

def executar_rotina_calculo(entrada: list[int], adicao: list[int], mutiplicacao: list[int], duplicados: list[int], impares: list[int], pares: list[int], primos: list[int]):
    if entrada:
        storage.armazenar_parametro(calculation.obter_adicao(entrada), adicao)
        storage.armazenar_parametro(calculation.obter_multiplicacao(entrada), mutiplicacao)
        lista_duplicados: list[int] = calculation.obter_duplicados(entrada)
        print(lista_duplicados)
        lista_impares: list[int] = calculation.obter_impares(entrada)
        print(lista_impares)
        lista_pares: list[int] = calculation.obter_pares(entrada)
        print(lista_pares)
        lista_primos: list[int] = calculation.obter_primos(entrada)
        print(lista_primos)

def exibir_listas(entrada: list[int], adicao: list[int], multiplicacao: list[int], duplicados: list[int], impares: list[int], pares: list[int], primos: list[int]):
      print(f"\n\nRol de entrada: {entrada}")
      print(f"Total de adição: {adicao}")
      print(f"Total de multiplicação: {multiplicacao}")
      print(f"Lista de duplicados: {duplicados}")
      print(f"Lista de ímpares: {impares}")
      print(f"Lista de pares: {pares}")
      print(f"Lista de primos: {primos}")


executar_rotina_entrada(entrada)
executar_rotina_calculo(entrada, adicao, multiplicacao, duplicados, impares, pares, primos)
exibir_listas(entrada, adicao, multiplicacao, duplicados, impares, pares, primos)