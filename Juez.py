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
PALABRA = rf"(?:{STRING}|{caracteres_permitidos}|{digitos})"


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
    ValidezEstrofa= True

    while i<len(Estrofas):
        Verso=[]
        if Estrofas[i] == "":
            i+=1
        while i < len(Estrofas) and Estrofas[i] != "":
            for caracter in Estrofas[i]:
                if not re.match(PALABRA, caracter):
                    ValidezEstrofa= False
            Verso.append(Estrofas[i])
            i+=1
        ListaEstrofas.append((Verso, ValidezEstrofa))
    # Cerrar el archivo 
    EstrofasArchivo.close()
    return  PalabrasBonus, ListaEstrofas

def ExtraerUltPalabraVerso(ListaEstrofas):
    ListaUltPalVersos=[]
    for versos, validez in ListaEstrofas:
        if len(versos) == 4:
            UltimasPalabras= []
            for palabra in versos: 
                palabras = palabra.strip().split()
                ultima = palabras[-1].strip(',.´\'"')
                UltimasPalabras.append(ultima)
            ListaUltPalVersos.append(UltimasPalabras)
    return ListaUltPalVersos

def TipoRima(palabra1, palabra2):
    p1= palabra1
    p2= palabra2
    print(p1,p2)


    #----GEMELA----
    if re.match(p1,p2):
        return "Gemela"
    
    #----CONSONANTE----
    # Rango desde la long completa de p1 hasta la 3ra letra, y empieza desde atras (-1)
    for i in range(len(p1), 2, -1):
        concidencia = re.match(PALABRA, p1[-i:])
        if concidencia:
            sufijo= concidencia.group()
            if re.search(sufijo, p2):
                CantidadLetras=len(sufijo)
                return "Consonante", CantidadLetras
    
   #----ASONANTE----
    VocalesP1 = ""
    VocalesP2 = ""
    for vocal in re.findall(vocales, p1):
        VocalesP1 += vocal

    for vocal in re.findall(vocales, p2):
        VocalesP2 += vocal

    print(VocalesP1, VocalesP2)
    VocalesIguales= ""
    ContadorVocales= 0
    for i in range(1, min(len(VocalesP1), len(VocalesP2)) + 1):
        if VocalesP1[-i]==VocalesP2[-i]:
            VocalesIguales= VocalesP1[-i] + VocalesIguales
            ContadorVocales +=1
        else:
            break
    
    if VocalesIguales and re.search(VocalesIguales, VocalesP2):
        return "Asonante", CantidadLetras
    
    


def IDRimas(ListaUltPalabraVersos):
    Puntaje= 0
    for palabra in ListaUltPalabraVersos:
        v1, v2, v3, v4 = palabra
        print(v1, v2, v3, v4)

      

        pares = [(v1,v2),(v1,v3),(v1,v4),(v2,v3),(v2,v4),(v3,v4)]
        
        for a,b in pares:
            Tipo, CoincidenciaLetras = TipoRima(a,b)
            if Tipo == "Consonante" and CoincidenciaLetras <= 4:
                Puntaje +=5
            else:

                puntaje += 5
            elif tipo == "asonante":
                puntaje += 5
            # ninguna → 0 pts
            
        Puntaje.append(puntaje)
    
    return Puntaje

   
    


def ArchivoSalida(nombre_archivo):

    PalabrasBonus, ListaEstrofas = IdentificarEstrofas(nombre_archivo)
    ArchSalida= "decision.txt"
    ArchSalida= open(ArchSalida,"w", encoding="utf-8")

    i=1
    for verso, validez in  ListaEstrofas:
        if len(verso) != 4 or validez == False:
            escribir=f"Estrofa {i}: Inválida" 
        else:
            escribir=f"Estrofa {i}: Válida"
        
        ArchSalida.write(escribir+"\n")
        i+=1         
    

# Imprimir el contenido
#print(IdentificarEstrofas("estrofas.txt"))
PalabrasBonus, ListaEstrofas = IdentificarEstrofas("estrofas.txt")
#print(PalabrasBonus)
#print(ListaEstrofas)
ListaUltPalabraVersos= ExtraerUltPalabraVerso(ListaEstrofas)
print(ListaUltPalabraVersos)
#print(IdentificarRimas(ListaUltPalabraVersos))
v1="malambo"
v2="mangos"
print(TipoRima(v1,v2))
print(ArchivoSalida("estrofas.txt"))



