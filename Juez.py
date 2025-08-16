#Importacion Modulo
import re 

'''
EBNF General
digitos ::= ([0-9])
vocal ::= (AEIOU|aeiou)
vocal_acentuada ::= (ÁÉÍÓÚ|áéíóú)
letras ::= ([A-Z|a-z|Ññ])
string ::= (<vocal>|<vocal_acentuada>|<letras>)
caracteres_permitidos ::= (’¿’|’ ?’|’¡’|’ !’|’,’|’.’|’;’| ’ |’-’|’(’|’)’|’:’| ")
palabra ::= (<string>|<caracteres_permitidos>|<digitos>)
'''

digitos = r"[0-9]"
vocal = r"[AEIOUaeiou]"
vocal_acentuada = r"[ÁÉÍÓÚáéíóú]"
letras = r"[A-Za-zÑñ]"

string = f"(?:{vocal}|{vocal_acentuada}|{letras})+"
caracteres_permitidos = r"[¿?¡!.,;\-():\" \s]"
palabra = f"(?:{string}|{caracteres_permitidos}|{digitos})"

# Abrir el archivo en modo lectura
EstrofasArchivo = open("estrofas.txt", "r", encoding="utf-8")

# Leer todo el contenido
ContenidoArchivo = EstrofasArchivo.read()

# Imprimir el contenido
# print(ContenidoEstrofas)

# Cerrar el archivo para liberar recursos
EstrofasArchivo.close()
