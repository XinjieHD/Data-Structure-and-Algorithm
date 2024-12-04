class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def operate(op, b, a):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return int(a / b)

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                stack.append(operate(token, b, a))
            else:
                stack.append(int(token))
        
        return stack[0]
