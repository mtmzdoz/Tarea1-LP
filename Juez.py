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
vocales = r"[AEIOUaeiouÁÉÍÓÚáéíóú]"
letras = r"[A-Za-zÑñ]"
caracteres_permitidos = r"[¿?¡!.,;\-():\" \s]"

STRING = rf"(?:{vocales}|{letras})+"
PALABRA = rf"(?:{string}|{caracteres_permitidos}|{digitos})"


def IdentificarEstrofas(nombre_archivo):
    # Abrir el archivo en modo lectura
    EstrofasArchivo = open(nombre_archivo, "r", encoding="utf-8")
    ContenidoArchivo = EstrofasArchivo.read()
    
    Estrofas= ContenidoArchivo.strip().split("\n")
    # Se identifican palabras bonus fresco, mangos, melón, cielo. Linea 1
    if ("," in Estrofas[0] and Estrofas[1].strip()== "") or Estrofas[1].strip()== "":
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

def ExtraerUltPalabraVerso(ListaEstrofas):
    ListaUltPalVersos=[]
    for versos in ListaEstrofas:
        if len(versos) == 4:
            UltimasPalabras= []
            for palabra in versos: 
                palabras = palabra.strip().split()
                ultima = palabras[-1].strip(',.´\'"')
                UltimasPalabras.append(ultima)
            ListaUltPalVersos.append(UltimasPalabras)
    return ListaUltPalVersos

def Palabralimpia(palabra):
    letras=re.findallall(PALABRA,palabra)
    letras= letras.join(letras)
    return letras

def TipoRima(palabra1, palabra2):
    p1= Palabralimpia(palabra1)
    p2= Palabralimpia(palabra2)

    if re.search(f"{palabra1}", palabra2):
        return "consonante"

def IdentificarRimas(ListaUltVersos):
    Puntaje= []

    for palabra in ListaUltVersos:
         v1, v2, v3, v4 = palabra
         print(v1, v2, v3, v4)
        
    return v1, v2, v3, v4
""""
        pares = [(v1,v2),(v1,v3),(v1,v4),(v2,v3),(v2,v4),(v3,v4)]
        
        for a,b in pares:
            tipo = TipoRima(a,b)
            if tipo == "consonante":
                # Coincidencia 3-4 letras → 5 pts (puedes ajustar n_consonante)
                puntaje += 5
            elif tipo == "asonante":
                puntaje += 5
            # ninguna → 0 pts
            
        Puntajes.append(puntaje)
    
    return Puntajes
"""
    
    


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
#print(IdentificarEstrofas("estrofas.txt"))
ListaEstrofas = IdentificarEstrofas("estrofas.txt")
ListaUltPalabraVersos= ExtraerUltPalabraVerso(ListaEstrofas)
print(ListaUltPalabraVersos)
print(IdentificarRimas(ListaUltPalabraVersos))
v1 = "escabiando"
v2 = "flotando"
#print(TipoRima(v1, v2))
#print(ArchivoSalida("estrofas.txt"))



