class MathTutor:
    def __init__(self):
        self.operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        }
        
    def explain_operation(self, operator):
        explanation = {
            '+': "Addition adds two numbers together.",
            '-': "Subtraction subtracts the second number from the first.",
            '*': "Multiplication gives the product of two numbers.",
            '/': "Division divides the first number by the second.",
        }
        return explanation.get(operator, "Invalid operation.")
    
    def perform_operation(self, operator, a, b):
        if operator in self.operations:
            return self.operations[operator](a, b)
        else:
            return None
if __name__ == "__main__":
    tutor = MathTutor()
    # Example usage:
    operator = '+'
    a, b = 10, 5
    print(tutor.explain_operation(operator))
    result = tutor.perform_operation(operator, a, b)
    print(f"Result of {a} {operator} {b} = {result}")