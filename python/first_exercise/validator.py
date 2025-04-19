def validar_entrada(entrada:str) -> int:
    teste:str = entrada
    try:
        numero:int = int(teste)
        return numero
    except ValueError:
        print("\nNão foi possível identificar um número inteiro."
              "\nTente novamente.")
        return None