class Solution:
    def calculate(self, s: str) -> int:
        stack = []  
        current_number = 0
        current_result = 0
        sign = 1 
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                current_result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                current_result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1
            elif char == ')':
                current_result += sign * current_number
                current_number = 0
                current_result *= stack.pop()  
                current_result += stack.pop() 

        current_result += sign * current_number
        return current_result
