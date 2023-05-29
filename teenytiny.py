from lex import *

def main():
    source = "LET foobar = 123"
    lexer = Lexer(source)

    while lexer.peekChar() != '\0':
        print(lexer.curChar)
        lexer.nextChar()

#call main
main()
