import ply.yacc as yacc
from analizadorLex import tokens


#Inicio Alejandro Paz               
def p_prueba(p):
    '''prueba : VAR INTEGERS'''

#Fin Alejandro Paz
''' Completo '''



#Inicio Lenin Freire

#Fin Lenin Freire





#Inicio Kevin Bautista

#Fin Kevin Bautista





#Pruebas

parser = yacc.yacc()

data = '''
var saludo:Boolean=true
'''
#with open("testFile.txt", "r") as archivo:
#    data = archivo.read()

parser.parse(data)
