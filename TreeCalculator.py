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
    
class Node:
    def __init__(self,value,right=None, left=None):
        self.right = right
        self.left = left
        self.value = value

class AST:
    root = None
    def create_tree(self, sentence):
        stack = []
        for char in sentence:
            if not is_operator(char):
                node = Node(char)
                stack.append(node)
            else:
                node = Node(char)
                child1 = stack.pop()
                child2= stack.pop()
                node.right = child1
                node.left = child2
                stack.append(node)
        node = stack.pop()
        self.root = node
    
    def calculate_exp(self, root):
       if not root:
           return 0
       if(not root.left and not root.right):
           return float(root.value)
       l_val = self.calculate_exp(root.left)
       r_val = self.calculate_exp(root.right)
       if root.value =="+":
           return l_val+r_val
       if root.value =="-":
           return l_val-r_val
       if root.value == "*":
           return l_val*r_val
       if root.value =="/":
           return l_val/r_val

filename = "code.txt"      
parser = Parser(filename)
expression, variables = parser.parse_expression()
exp = parser.tranform_expression(expression, variables)
print(expression)
tree = AST()
tree.create_tree(exp)
print("Result:" + str(tree.calculate_exp(tree.root)))

