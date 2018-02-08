
import ply.yacc as yacc
from plytest import tokens


def p_num_plus(p):
    'num : num PLUS num'
    p[0] = p[1] + p[3]


def p_num_num(p):
    'num : NUMBER'
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
