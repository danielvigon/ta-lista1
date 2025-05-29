class InputModel:

    def __init__(self):
        self.var_inputs: list[int] = []
    
    def read_input(self) -> str:
        var_input:str = input("\n👋 Forneça números inteiros para comporem uma lista (0 encerra a lista para executar cálculos): ")
        return var_input

    def validate_input(self, var_input: str) -> int:
        try:
            var_number: int = int(var_input)
            return var_number
        except ValueError:
            print("\n❌ Ops, não foi possível identificar um número inteiro."
                  "\n👇 Forneça novamente.")
            return 0

    def storage_input(self, input: str):
        self.var_inputs.append(input)

    def execute_routine(self):
        var_input: str = self.read_input()
        var_number: int = self.validate_input(var_input)

        if var_input == '0':
                return
        elif var_number == 0:
                self.execute_routine()
        else:
                self.storage_input(var_number)
                self.execute_routine()