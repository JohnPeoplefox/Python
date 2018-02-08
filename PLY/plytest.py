
import ply.lex as lex


tokens = ('NUMBER', 'PLUS',)
t_PLUS    = r'\+'
t_ignore  = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
