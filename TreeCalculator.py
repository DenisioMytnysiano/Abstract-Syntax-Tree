def is_operator(c):
    if (c == '+' or c == '-' or c == '*'
        or c == '/' or c == '^'): 
        return True
    else: 
        return False
        
def parse_equation(equation):
    OPERATORS = ['+', '-', '/', '*', '(', ')']
    result = ''
    for char in equation:
        if char in OPERATORS:
            char = ' ' + char + ' '
        result += char
    while '  ' in result:
        result = result.replace('  ', ' ')
    return result.strip()
    
def shunting_yard(sentence):
    op = {'+': 1, '-':1, '*': 2, '/':2}
    stack = []
    formula = []
    for token in sentence:
        if token in op: 
            while stack and stack[-1] != "(" and op[token] <= op[stack[-1]]:
                formula.append(stack.pop())
            stack.append(token)
        elif token == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                formula.append(x)
        elif token == "(":
            stack.append(token)
        else:
            formula.append(token)
    while stack:
        formula.append(stack.pop())
    return formula

class Parser:
    def __init__(self, filename):
        self.filename = filename
    def parse_expression(self):
        variables = dict()
        expression = ""
        with open(self.filename, "r") as file:
            data = file.read().splitlines()
        expression = data[-1].replace(";", "")
        for x in range(len(data)-1):
            row = data[x].replace(";", "").split(" ")
            variables[row[0]] = row[2]
        expression = parse_equation(expression)
        return (expression, variables)
    def tranform_expression(self, expression, variables):
        for var in variables:
            while var in expression:
                expression = expression.replace(var, variables[var])
        return shunting_yard(expression.split(" "))
filename = "code.txt"       