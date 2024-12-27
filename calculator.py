from typing import Union

# Define calculator class
class Calculator:
    def __init__(self):
        pass

    def divide(self, number1: Union[int, float], number2: Union[int, float]):
        '''Divide two numbers

        Parameter: 
            number1: int or float, first number for division
            number2: int or float, second number for division

        Returns:
            float, division result
        '''
        self.a = number1
        self.b = number2

        try:
            self.result = self.a / self.b

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")

        return self.result
    

    def multiply(self, number1: Union[int, float], number2: Union[int, float]):
        '''Multiply two numbers
        
        Parameter:
            number1: int or float, first number for multiplication
            number2: int or float, second number for multiplication
        
        Returns:
            float, multiplication result'''
        
        self.a = number1
        self.b = number2

        if isinstance(self.a, str) or isinstance(self.b, str):
            raise TypeError("Only numbers are allowed")
        
        self.result = self.a * self.b
        return self.result
    
    def sum(self, number1: Union[int, float], number2: Union[int, float]):
        '''Sum two numbers
        
        Parameter:
            number1: int or float, first number for sum
            number2: int or float, second number for sum
        
        Returns:
            float, sum result'''
        
        self.a = number1
        self.b = number2

        try: 
            self.result = self.a + self.b
        except TypeError as e:
            print(f"Error: {e}")
        
        return self.result
    
    def subtract(self, number1: Union[int, float], number2: Union[int, float]):
        '''Subtract two numbers
        
        Parameter:
            number1: int or float, first number for subtraction
            number2: int or float, second number for subtraction
            
        Returns:
            float, subtraction result'''
        
        self.a = number1
        self.b = number2

        try:
            self.result = self.a - self.b
        
        except TypeError as e:
            print(f'Error: {e}')

        return self.result