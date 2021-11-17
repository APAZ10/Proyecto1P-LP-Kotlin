import ply.yacc as yacc
from analizadorLex import tokens


#Inicio Alejandro Paz
''' Completo var saludo:Boolean=true'''

def p_asignacion_boolean(p):
    '''asignacionBoolean : VAR NAME ':' BOOLEAN ASSIGN condicion
    '''

def p_condicion(p):
    '''condicion : booleanExpression
                | NOT condicion
                | condicion numberOperator condicion
                | condicion logicOperator condicion
    '''

def p_condicion_parentesis(p):
    '''condicion : LPARENTH condicion RPARENTH
    '''

def p_boolean_expression(p):
    '''booleanExpression : TRUE
                        | FALSE
                        | numberBooleanExpression
                        | stringBooleanExpression
    '''

def p_stringexpression(p):
    '''stringBooleanExpression : STRINGS stringOperator STRINGS
                                | CHARS stringOperator CHARS
    '''

def p_numberexpression(p):
    '''numberBooleanExpression : number numberOperator number
    '''

def p_number(p):
    '''number : INTEGERS
            | DECIMALS
    '''

def p_numberoperator(p):
    '''numberOperator : EQUALS
                    | NOTEQUALS
                    | LOWER
                    | LOWEREQUAL
                    | GREATER
                    | GREATEREQUAL
    '''

def p_logicoperator(p):
    '''logicOperator : AND
                    | OR
    '''

def p_stringoperator(p):
    '''stringOperator : EQUALS
                    | NOTEQUALS
    '''

#Fin Alejandro Paz




#Inicio Lenin Freire

#Fin Lenin Freire





#Inicio Kevin Bautista

#Fin Kevin Bautista





#Pruebas

parser = yacc.yacc()

data = '''
var saludo:Boolean=(!(1<10)&&(1>0)||('a'=='a'))
'''
#with open("testFile.txt", "r") as archivo:
#    data = archivo.read()

parser.parse(data)
