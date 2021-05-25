from BukoPyInterpreter import *
from BukoPySymbolTable import *

#######################################
# RUN
#######################################

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number(0))


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    print(tokens)

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error


def main():
    while True:
        text = input('BukoPy >> ')
        result, error = run('<stdin>', text)

        if error:
            print(error.as_string())
            continue

        print(result)


if __name__ == '__main__':
    main()
