import ply.yacc as yacc
from analizadorLex import tokens

def p_sentencia(p):
    '''statement : asignacion
                    | metodos
    '''
def p_metodos(p):
    '''metodos : metodoAddLista
                | metodoRemoveLista
                | equalsString
                | metodoPlus
    '''
#Inicio Alejandro Paz
''' Asignacion Booleana, '''

def p_asignacion(p):
    '''asignacion : asignacionBoolean
                    | asignacionInt
                    | asignacionString
                    | asignacionChar
                    | asignacionLista
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
                                | equalsString
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
'''Asignacion String'''

def p_asignacion_string(p):
    '''asignacionString : tipoVariable NAME ':' STRING ASSIGN resultadoString
                        | tipoVariable NAME ASSIGN resultadoString
                        | NAME ASSIGN resultadoString
    '''

def p_resultadostring(p):
    '''resultadoString : tipoString
                        | metodoPlus
                        | LPARENTH resultadoString RPARENTH
    '''

'''Metodo Plus String'''

def p_metodoplusstring(p):
    '''metodoPlus : resultadoString PLUS resultadoString
                    | resultadoString "." PLUSSTRING LPARENTH resultadoString RPARENTH
                    | NAME "." PLUSSTRING LPARENTH resultadoString RPARENTH
    '''

def p_tipostring(p):
    '''tipoString : STRINGS
                    | NAME
    '''

'''Metodo Equals String'''

def p_metodoequalsstring(p):
    '''equalsString : resultadoString "." EQUALSSTRING LPARENTH resultadoString RPARENTH
                    | NAME "." EQUALSSTRING LPARENTH resultadoString RPARENTH
    '''

#Fin Lenin Freire

#Inicio Kevin Bautista
def p_asignacion_char(p):
    '''asignacionChar : tipoVariable NAME ':' CHAR ASSIGN CHARS
                        | tipoVariable NAME ASSIGN CHARS
                        | NAME ASSIGN CHARS
    '''

def p_asignacion_lista(p):
    '''asignacionLista : tipoVariable NAME ASSIGN LIST LOWER todoTipoDato GREATER LPARENTH RPARENTH
                        | tipoVariable NAME ASSIGN LIST LOWER todoTipoDato GREATER LPARENTH contenidoLista RPARENTH
                        | tipoVariable NAME ASSIGN LIST LPARENTH contenidoLista RPARENTH
    '''

def p_metodo_add_lista(p):
    '''metodoAddLista : NAME "." ADD LPARENTH item RPARENTH
    '''

def p_metodo_remove_lista(p):
    '''metodoRemoveLista : NAME "." REMOVEAT LPARENTH INTEGERS RPARENTH
    '''

def p_item(p):
    '''item : number
            | STRINGS
            | CHARS
    '''

def p_contenido_lista(p):
    '''contenidoLista : contenidoListaNumerica
                         | contenidoListaString
    '''

def p_contenido_lista_numeric(p):
    '''contenidoListaNumerica : number
                                | number "," contenidoListaNumerica
    '''

def p_contenido_lista_string(p):
    '''contenidoListaString : STRINGS
                            | STRINGS "," contenidoListaString
    '''

def p_todo_tipo_dato(p):
    '''todoTipoDato : tipoDatoNumerico
                    | STRING
                    | CHAR           
    '''
    #| BOOLEAN



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