class ContainerModel:
    
    def __init__(self):
        self.total_sum: list[int] = []
        self.total_product: list[int] = []
        self.duplicated: list[int] = []
        self.distinct_odd: list[int] = []
        self.distinct_even: list[int] = []
        self.distinct_prime: list[int] = []

    def show_lists(self):
        print("\n\n")
        print(f"📋 Total de soma: {self.total_sum}")
        print(f"📋 Total de produto: {self.total_product}")
        print(f"📋 Lista de duplicados: {self.duplicated}")
        print(f"📋 Lista de ímpares distintos: {self.distinct_odd}")
        print(f"📋 Lista de pares distintos: {self.distinct_even}")
        print(f"📋 Lista de primos distintos: {self.distinct_prime}")