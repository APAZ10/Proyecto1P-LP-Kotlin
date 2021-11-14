from re import M
from ply import lex

reserved = {
    #Inicio Alejandro Paz
    'class':'CLASS',
    'fun':'FUN',
    'true':'TRUE',
    'as':'AS',
    'continue':'CONTINUE',
    'if':'IF',
    'break':'BREAK',
    'null':'NULL',
    'return':'RETURN',
    'val':'VAL',
    'var':'VAR',
    'while':'WHILE',
    'else':'ELSE',
    'for':'FOR',
    'false':'FALSE',
    'mutableListOf': 'LIST',
    'add': 'ADD',
    'removeAt': 'REMOVEAT',
    #Fin Alejandro Paz

    #Inicio Lenin Freire
    'package':'PACKAGE',
    'super':'SUPER',
    'this':'THIS',
    'throw':'THROW',
    'try':'TRY',
    'do':'DO',
    'in':'IN',
    'interface':'INTERFACE',
    'is':'IS',
    'object':'OBJECT',
    'typeof':'TYPE',
    'when':'WHEN',
    'typealias':'TYPEALIAS',
    'true':'TRUE',
    'by':'BY',
    'setOf':'SET',
    'isEmpty':'EMPTY',
    'contains':'CONTAINS',
    #Fin Lenin Freire


    #Inicio Kevin Bautista

    #Fin Kevin Bautista
}


tokens = (
    #Inicio Alejandro Paz
    'ASSIGN', 'ASSIGNPLUS', 'ASSIGNMINUS', 'INCREMENT', 'DECREMENT',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVISION', 'MODULO',
    #Fin Alejandro Paz

    #Inicio Lenin Freire
    'GREATER', 'GREATEREQUAL', 'LOWER', 'LOWEREQUAL', 'EQUALS', 'NOT',
    'NOTEQUALS', 'AND', 'OR',
    #Fin Lenin Freire

    #Inicio Kevin Bautista

    'INTEGERS', 'DECIMALS', 'NAME'
    #Fin Kevin Bautista
) + tuple(reserved.values())


#Inicio Alejandro Paz
t_ASSIGN = r'\='
t_ASSIGNPLUS = r'\+\='
t_ASSIGNMINUS = r'\-\='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVISION = r'\/'
t_MODULO = r'\%'
#Fin Alejandro Paz

#Inicio Lenin Freire
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>\='
t_LOWER = r'\<'
t_LOWEREQUAL = r'\<\='
t_EQUALS = r'\=\='
t_NOT = r'\!'
t_NOTEQUALS = r'\!\='
t_AND = r'\&\&'
t_OR = r'\|\|'
#Fin Lenin Freire


#Inicio Kevin Bautista

#Fin Kevin Bautista

#Inicio Alejandro Paz               #FALTA CORREGIR
def t_DECIMALS(t):
    r'(\-|\+)?\d+\.\d+'
    t.value = float(t.value[:-1])
    return t

def t_INTEGERS(t):
    r'(\-|\+)?\d+'
    t.value = int(t.value)
    return t

#Fin Alejandro Paz

#Inicio Lenin Freire

#Fin Lenin Freire


#Inicio Kevin Bautista

#Fin Kevin Bautista

#t_ignore = r' \t'               #FALTA CORREGIR

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Componente léxico no encontrado '%s'" % t.value[0])
    t.lexer.skip(1)

#Pruebas
lexer = lex.lex()

data = input("")
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)