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
    'println':'PRINTLN',
    'print':'PRINT',
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
    'by':'BY',
    'setOf':'SETOF',
    'isEmpty':'EMPTY',
    'contains':'CONTAINS',
    'Int':'INT',
    'Float':'FLOAT',
    'Double':'DOUBLE',
    'Char':'CHAR',
    'String':'STRING',
    'Byte':'BYTE',
    'Long':'LONG',
    'Short':'SHORT',
    'Boolean':'BOOLEAN',
    'readLine':'READLINE',
    #Fin Lenin Freire


    #Inicio Kevin Bautista
    'catch':'CATCH',
    'delegate':'DELEGATE',
    'set':'SET',
    'constructor':'CONSTRUCTOR',
    'dynamic':'DYNAMIC',
    'field':'FIELD',
    'file':'FILE',
    'finally':'FINALLY',
    'get':'GET',
    'import':'IMPORT',
    'init':'INIT',
    'param':'PARAM',
    'property':'PROPERTY',
    'receiver':'RECEIVER',
    'setparam':'SETPARAM',
    'value':'VALUE',
    'where':'WHERE',
    'plus':'PLUSSTRING',
    'equals':'EQUALSSTRING'
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
    'LPARENTH','RPARENTH','LBRACKET','RBRACKET','LCBRACKET',
    'RCBRACKET','INTEGERS', 'DECIMALS', 'NAME', 'STRINGS', 'CHARS' 
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
t_LPARENTH = r'\('
t_RPARENTH = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
#Fin Kevin Bautista

literals = [',','.',':',';']

#Inicio Alejandro Paz               
def t_DECIMALS(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGERS(t):
    r'\d+'
    t.value = int(t.value)
    return t
    #borrado momentaneo del mas y menos
#Fin Alejandro Paz

#Inicio Lenin Freire
def t_NAME(t):
    r'(\_*[a-zA-Z]+[\_a-zA-Z0-9]*|\_+[0-9]+[\_a-zA-Z0-9]*)'

    t.type = reserved.get(t.value,'NAME')
    return t

#Fin Lenin Freire


#Inicio Kevin Bautista
def t_STRINGS(t):
    r'\"[^\n\"]*\"'
    t.type = reserved.get(t.value, 'STRINGS')
    return t

def t_CHARS(t):
    r'\'[^\n\']\''
    t.type = reserved.get(t.value,'CHARS')
    return t
#Fin Kevin Bautista


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Componente léxico no encontrado '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#Pruebas
'''
with open("testFile.txt", "r") as archivo:
    data = archivo.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)
'''

lexer.input("val numero=10 + 10")

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)