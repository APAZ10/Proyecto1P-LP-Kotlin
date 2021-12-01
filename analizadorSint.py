import ply.yacc as yacc
from analizadorLex import tokens

errors = []

def p_statement(p):
    '''statement : asignacion
                | metodos
                | estructuraIf
                | estructuraLoop
                | funcion
                | NAME INCREMENT
                | NAME DECREMENT
                | clase
                | statement statement
    '''
def p_metodos(p):
    '''metodos : metodoAddLista
                | metodoRemoveLista
                | equalsString
                | metodoPlus
                | metodoIsEmptyConjunto
                | metodoContainsConjunto
                | lectura
                | impresion
    '''
#Inicio Alejandro Paz

def p_clase(p):
    '''clase : CLASS NAME LPARENTH parameters RPARENTH LCBRACKET structureBody RCBRACKET
            | CLASS NAME LCBRACKET structureBody RCBRACKET
    '''

''' Asignacion Booleana, '''

def p_asignacion(p):
    '''asignacion : asignacionBoolean
                    | asignacionInt
                    | asignacionString
                    | asignacionChar
                    | asignacionLista
                    | asignacionConjunto
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
                | condicion logicOperator condicion
                | NAME
    '''

def p_condicion_parentesis(p):
    '''condicion : LPARENTH condicion RPARENTH
    '''

def p_boolean_expression(p):
    '''booleanExpression : TRUE
                        | FALSE
                        | numberBooleanExpression
                        | stringBooleanExpression
                        | metodoIsEmptyConjunto
                        | metodoContainsConjunto
    '''

def p_boolean_stringexpression(p):
    '''stringBooleanExpression : STRINGS stringOperator STRINGS
                                | CHARS stringOperator CHARS
                                | equalsString
    '''

def p_boolean_numberexpression(p):
    '''numberBooleanExpression : resultado numberOperator resultado
    '''

def p_number(p):
    '''number : INTEGERS
            | DECIMALS
            | NAME
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
                    | EQUALS
                    | NOTEQUALS
    '''

def p_stringoperator(p):
    '''stringOperator : EQUALS
                    | NOTEQUALS
    '''

''' Asignacion conjuntos '''
def p_asignacion_conjunto(p):
    '''asignacionConjunto : tipoVariable NAME ASSIGN SETOF LPARENTH contenidoLista RPARENTH
    '''
    # verificar mezcla de tipo de datos, y <>

def p_metodo_isempty_conjunto(p):
    '''metodoIsEmptyConjunto : NAME "." EMPTY LPARENTH RPARENTH
    '''

def p_metodo_contains_conjunto(p):
    '''metodoContainsConjunto : NAME "." CONTAINS LPARENTH contenidoMetodo RPARENTH
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
    '''resultadoString : STRINGS
                        | metodoPlus
                        | LPARENTH resultadoString RPARENTH
                        | lectura
                        | NAME
    '''

'''Metodo Plus String'''

def p_metodoplusstring(p):
    '''metodoPlus : resultadoString PLUS resultadoString
                    | resultadoString "." PLUSSTRING LPARENTH resultadoString RPARENTH
                    | NAME "." PLUSSTRING LPARENTH resultadoString RPARENTH
    '''

'''Metodo Equals String'''

def p_metodoequalsstring(p):
    '''equalsString : resultadoString "." EQUALSSTRING LPARENTH resultadoString RPARENTH
                    | NAME "." EQUALSSTRING LPARENTH resultadoString RPARENTH
    '''

'''Impresion de datos'''

def p_impresion(p):
    '''impresion : impresionTipo LPARENTH RPARENTH
                | impresionTipo LPARENTH contenidoPrint RPARENTH
    '''

def p_impresiontipo(p):
    '''impresionTipo : PRINTLN
                    | PRINT
    '''

def p_contenido(p):
    '''contenidoPrint : condicion
                    | resultado
                    | resultadoString
                    | item
    '''

'''Lectura de datos'''

def p_lectura(p):
    '''lectura : READLINE LPARENTH RPARENTH
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
            | NAME
    '''

def p_contenido_lista(p):
    '''contenidoLista : contenidoListaNumerica
                         | contenidoListaString
    '''

def p_contenido_metodo(p):
    '''contenidoMetodo : contenidoLista
                        | NAME
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

    '''ESTRUCTURA DE DATOS IF'''
def p_estructuraif(p):
    '''estructuraIf : IF LPARENTH condicion RPARENTH LCBRACKET structureBody RCBRACKET 
                    | IF LPARENTH condicion RPARENTH LCBRACKET structureBody RCBRACKET estructureElse
    '''
def p_estructuraelse(p):
    '''estructureElse : ELSE LCBRACKET structureBody RCBRACKET
    '''

def p_structurebody(p):
    '''structureBody : statement
                        | statement structureBody
    '''

    '''ESTRUCTURA LOOP'''
def p_estructuraloop(p):
    '''estructuraLoop : estructuraWhile
                    | estructuraFor
    '''

def p_estructurawhile(p):
    '''estructuraWhile : WHILE LPARENTH condicion RPARENTH LCBRACKET structureBody RCBRACKET
    '''

def p_estructurafor(p):
    '''estructuraFor : FOR LPARENTH NAME IN itemFor RPARENTH LCBRACKET structureBody RCBRACKET
    '''

def p_itemfor(p):
    '''itemFor : NAME
                | resultadoString
    '''

def p_funcion(p):
    '''funcion : FUN NAME LPARENTH parameters RPARENTH LCBRACKET structureFunction RCBRACKET 
                | FUN NAME LPARENTH RPARENTH LCBRACKET structureFunction RCBRACKET
                | FUN NAME LPARENTH parameters RPARENTH ":" todoTipoDato LCBRACKET structureFunction RCBRACKET 
                | FUN NAME LPARENTH RPARENTH ":" todoTipoDato LCBRACKET structureFunction RCBRACKET
    '''

def p_structurefunction(p):
    '''structureFunction : bodyFunction
                        | bodyFunction structureFunction
                        | RETURN contenidoPrint
    '''
    
def p_bodyfunction(p):
    '''bodyFunction : asignacion
                | metodos
                | estructuraIf
                | estructuraLoop
    '''

def p_parameters(p):
    '''parameters : parametersTipo
                | parametersTipo "," parameters
    '''
def p_parameterstipo(p):
    '''parametersTipo : NAME ":" todoTipoDato
    '''

#Fin Kevin Bautista

def p_error(p):
    if p:
        mssg= f'Syntax error at token {p.type} {p}'
    else:
        mssg= 'Syntax error at EOF'
    errors.append(mssg)



#Pruebas

parser = yacc.yacc()


#with open("testFile.txt", "r") as archivo:
#    s = archivo.read()



'''s = 
class Account {
    var acc: Int=0
    var name: String="mi cuenta"
    var amount: Float=3.56
    
    fun deposito(){
        print("Se ha realizado un deposito")
    } 
}
'''
#parser.parse(s)


'''
while True:
    try:
        s = input('valor > ')
    except EOFError:
        break
    if not s: continue

    parser.parse(s)
'''