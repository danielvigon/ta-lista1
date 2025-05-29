from input_model import InputModel
from container_model import ContainerModel
from calculation_helper import CalculationHelper

class Main:

    def __init__(self):
        self.input_instance: InputModel = InputModel()
        self.inputs_container: list[int] = self.input_instance.var_inputs
        self.container_instance: ContainerModel = ContainerModel()
        self.calculation_instance: CalculationHelper = CalculationHelper()

    def execute_input(self):
        self.input_instance.execute_routine()
        
    def execute_calculation(self):
        if self.inputs_container:
            self.container_instance.total_sum = self.calculation_instance.get_addition(self.inputs_container)
            self.container_instance.total_product = self.calculation_instance.get_multiplication(self.inputs_container)

    def main(self):
        self.execute_input()
        self.execute_calculation()
        self.container_instance.show_lists()


if __name__ == "__main__":
    Main().main()