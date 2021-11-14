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
    'removeAt': 'REMOVEAT'
    #Fin Alejandro Paz

    #Inicio Lenin Freire

    #Fin Lenin Freire


    #Inicio Kevin Bautista

    #Fin Kevin Bautista
}


tokens = (
    'INTS', 'DOUBLES', 'FLOATS', 'NAME'
) + tuple(reserved.values())


#Inicio Alejandro Paz

#Fin Alejandro Paz

#Inicio Lenin Freire

#Fin Lenin Freire


#Inicio Kevin Bautista

#Fin Kevin Bautista


#Pruebas
lexer = lex.lex()

data = input("")
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)