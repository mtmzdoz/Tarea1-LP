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


def IdentificarEstrofas(nombre_archivo):
    # Abrir el archivo en modo lectura
    EstrofasArchivo = open(nombre_archivo, "r", encoding="utf-8")
    
    ContenidoArchivo = EstrofasArchivo.read()
    
    
    Estrofas= ContenidoArchivo.strip().split("\n")
    # Se detecta Palabras bonus fresco, mangos, melón, cielo. Linea 1
    if "," in Estrofas[0] and Estrofas[1].strip()== "":
        PalabrasBonus= Estrofas[0]
        i=2
    else:
        i=0

    ListaEstrofas = []
    while i<len(Estrofas):
        Verso=[]
        if Estrofas[i] == "":
            i+=1
        while i < len(Estrofas) and Estrofas[i] != "":
            Verso.append(Estrofas[i])
            i+=1
        ListaEstrofas.append(Verso)
    
    
   
    # Cerrar el archivo 
    EstrofasArchivo.close()
    return ListaEstrofas

def ArchivoSalida(nombre_archivo):

    ListaEstrofas = IdentificarEstrofas(nombre_archivo)
    ArchSalida= "decision.txt"
    ArchSalida= open(ArchSalida,"w", encoding="utf-8")

    i=1
    for verso in ListaEstrofas:
        if len(verso) != 4:
            escribir=f"Estrofa {i}: Inválida" 
        else:
            escribir=f"Estrofa {i}: Válida"
        
        ArchSalida.write(escribir+"\n")
        i+=1         
    

# Imprimir el contenido
# print(ContenidoEstrofas)
print(IdentificarEstrofas("estrofas.txt"))
print(ArchivoSalida("estrofas.txt"))



