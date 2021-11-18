import ply.yacc as yacc
from analizadorLex import tokens

def p_sentencia(p):
    '''statement : asignacion
    '''

#Inicio Alejandro Paz
''' Asignacion Booleana, '''

def p_asignacion(p):
    '''asignacion : asignacionBoolean
                    | asignacionInt
    '''

def p_asignacion_boolean(p):
    '''asignacionBoolean : tipoVariable NAME ':' BOOLEAN ASSIGN condicion
                            | tipoVariable NAME ASSIGN condicion
                            | NAME ASSIGN condicion
    '''

def p_tipo(p):
    '''tipoVariable : VAR
                    | VAL
    '''

def p_condicion(p):
    '''condicion : booleanExpression
                | NOT condicion
                | condicion numberOperator condicion
                | condicion logicOperator condicion
                | resultado numberOperator resultado
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

def p_boolean_stringexpression(p):
    '''stringBooleanExpression : STRINGS stringOperator STRINGS
                                | CHARS stringOperator CHARS
    '''

def p_boolean_numberexpression(p):
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
''' Asignacion Numerica, '''

def p_asignacion_int(p):
    '''asignacionInt : tipoVariable NAME ':' tipoDatoNumerico ASSIGN resultado
                        | tipoVariable NAME ASSIGN resultado
                        | NAME ASSIGN resultado
                        | NAME ASSIGNMINUS resultado
                        | NAME ASSIGNPLUS resultado
    '''

def p_tipodatonumerico(p):
    '''tipoDatoNumerico : FLOAT
                        | INT
                        | DOUBLE
                        | BYTE
                        | LONG
                        | SHORT
    '''

def p_resultado(p):
    '''resultado : number
                    | resultado matOperator resultado
    '''

def p_resultado_parentesis(p):
    '''resultado : LPARENTH resultado RPARENTH
    '''

def p_matoperator(p):
    '''matOperator : PLUS
                    | MINUS
                    | MULTIPLY
                    | DIVISION
                    | MODULO
    '''
#Arreglar problemas con menos y mas

#Fin Lenin Freire





#Inicio Kevin Bautista
''' , '''



#Fin Kevin Bautista





#Pruebas

parser = yacc.yacc()

#data = '''
#var saludo:Boolean=(!(1<10)&&(1>0)||('a'=='a'))
#'''
#data = '''
#var numero=1
#'''
#with open("testFile.txt", "r") as archivo:
#    data = archivo.read()

#parser.parse(data)

while True:
   try:
       s = input('valor > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)