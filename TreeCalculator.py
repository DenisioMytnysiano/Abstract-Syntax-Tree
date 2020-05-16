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

filename = "code.txt"       