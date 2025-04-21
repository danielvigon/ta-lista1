def validar_entrada(entrada: str) -> int:
    try:
        numero: int = int(entrada)
        return numero
    except ValueError:
        print("\nNão foi possível identificar um número inteiro."
              "\nTente novamente.")
        return None