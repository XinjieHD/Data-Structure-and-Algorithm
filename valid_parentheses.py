class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ['(','{','[']
        close_list = [')', '}', ']']
        stack = []


        for char in s:
            if char in open_list:
                stack.append(char)
            elif char in close_list:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ')':
                        return False
                if current_char == '[':
                    if char != ']':
                        return False
                if current_char == '{':
                    if char != '}':
                        return False
        return not stack
