class CalculationHelper:

    def get_addition(self, var_list: list[int], var_index: int = 0, total: list[int] = [0]) -> list[int]:
        if var_index == len(var_list):
            return total
        else:
            total[0] += var_list[var_index]
            return self.get_addition(var_list, var_index + 1, total)

    def get_multiplication(self, var_list: list[int], var_index: int = 0, total: list[int] = [1]) -> list[int]:
        if var_index == len(var_list):
            return total
        else:
            total[0] *= var_list[var_index]
            return self.get_multiplication(var_list, var_index + 1, total)


        






