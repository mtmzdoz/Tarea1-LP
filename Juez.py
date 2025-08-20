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
        PalabrasBonus = "No hay"
        i=0

    ListaEstrofas = []
    

    while i<len(Estrofas):
        Verso=[]
        ValidezEstrofa= True
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

def ExtraerUltPalabra(PalabrasBonus, ListaEstrofas):
    UltPalVersos=[]
    

    for versos, validez in ListaEstrofas:
        if len(versos) == 4:
            UltimasPalabras= []
            for palabra in versos: 
                palabras = palabra.strip().split()
                ultima = palabras[-1].strip(',.´\'"')
                UltimasPalabras.append(ultima)

            Bonus = 0
            for ultima in UltimasPalabras:
                if ultima in PalabrasBonus:
                    Bonus = 2
                    break 
            
            UltPalVersos.append((UltimasPalabras, Bonus))

    return UltPalVersos

def TipoRima(palabra1, palabra2):
    p1= palabra1
    p2= palabra2
    print(p1,p2)

    Rima=[]
    Puntaje=0
    #----GEMELA----
    if re.match(p1,p2):
        Puntaje=1
        return "Gemela", Puntaje
    
    #----CONSONANTE----
    # Rango desde la long completa de p1 hasta la 3ra letra, y empieza desde atras (-1)
    for i in range(len(p1), 2, -1):
        concidencia = re.match(PALABRA, p1[-i:])
        if concidencia:
            sufijo= concidencia.group()
            if re.search(sufijo, p2):
                CantidadLetras=len(sufijo)
                if CantidadLetras == 3 or CantidadLetras== 4:
                    Puntaje = 5
                else:
                    Puntaje=8
                Rima.append(("Consonante", Puntaje))
    
   #----ASONANTE----
    VocalesP1 = ""
    VocalesP2 = ""
    for vocal in re.findall(vocales, p1.lower()):
        VocalesP1 += vocal

    for vocal in re.findall(vocales, p2.lower()):
        VocalesP2 += vocal

    #print(VocalesP1, VocalesP2)

    VocalesIguales= ""
    ContadorVocales= 0
    for i in range(1, min(len(VocalesP1), len(VocalesP2)) + 1):
        if VocalesP1[-i]==VocalesP2[-i]:
            VocalesIguales= VocalesP1[-i] + VocalesIguales
            ContadorVocales +=1
    
    #print(VocalesIguales, ContadorVocales)

    if VocalesIguales and re.search(VocalesIguales, VocalesP2):
        if ContadorVocales == 1:
            Puntaje=3
        elif ContadorVocales == 2:
            Puntaje= 4
        elif ContadorVocales >= 3:
            Puntaje=8
        Rima.append(("Asonante", Puntaje))
    
    MejorRima= None
    for rima in Rima:
        if rima[0] in ("Consonante", "Asonante"):
            if MejorRima is None or rima[1]> MejorRima[1]:
                MejorRima = rima
    
    if MejorRima:
        return MejorRima
    
    #----MISMA TERMINACIÓN----
    for i in range(min(len(p1), len(p2)), 1, -1):
        coincidencia= p1[-i:]
        if re.search(coincidencia,p2):
            CantidadLetras= len(coincidencia)
            if CantidadLetras >= 2:
                Puntaje=2
            return "Misma Terminación", Puntaje
    
    return "No Riman", 0


def IDRimas(ListaUltPalabraVersos):
    
    Resultado= []

    for palabra, bonus in ListaUltPalabraVersos:
        v1, v2, v3, v4 = palabra
        #print(v1, v2, v3, v4)

        pares = [(v1,v2),(v1,v3),(v1,v4),(v2,v3),(v2,v4),(v3,v4)]

        TotalPuntaje= 0
        RimaFinal= []
    

        for a,b in pares:
            Tipo, Puntos = TipoRima(a,b)
            print(Tipo, Puntos)
            if Tipo != "No Riman":
                TotalPuntaje += Puntos
                Descuento = False
            elif Tipo == "No Riman":
                Descuento = True 
            if Tipo not in RimaFinal:
                RimaFinal.append(Tipo)
        
        if Descuento:
            TotalPuntaje -=2

        print(TotalPuntaje)
        TotalPuntaje= (TotalPuntaje + bonus )/5
        Resultado.append((RimaFinal, TotalPuntaje, bonus))

        print (Resultado)
    return Resultado

   
def ArchivoSalida(nombre_archivo):

    PalabrasBonus, ListaEstrofas = IdentificarEstrofas(nombre_archivo)
    ListaUltPalabraVersos = ExtraerUltPalabra(PalabrasBonus, ListaEstrofas)
    Resultado = IDRimas(ListaUltPalabraVersos)

    ArchSalida= "decision.txt"
    ArchSalida= open(ArchSalida,"w", encoding="utf-8")

    i=1
    indice_resultado=0
    for verso, validez in ListaEstrofas:
        RimaFinal, TotalPuntos, Bonus = Resultado[indice_resultado]

        if len(verso) != 4 or validez == False:
            ArchSalida.write("Estrofa {0}: Inválida\n".format(i))
        else:
            Ptos = f"{TotalPuntos:.1f}/10"
            if  Bonus > 0:
                ArchSalida.write("Estrofa {}: {} (BONUS)\n".format(i, Ptos))
            else:
                ArchSalida.write("Estrofa {}: {}\n".format(i, Ptos))
            if RimaFinal:
                ArchSalida.write("Rimas: " + ", ".join(RimaFinal) + "\n")
            indice_resultado +=1
        i+=1
    ArchSalida.close()

PalabrasBonus, ListaEstrofas = IdentificarEstrofas("estrofas.txt")
ListaUltPalabraVersos = ExtraerUltPalabra(PalabrasBonus, ListaEstrofas)
v1="desierto"
v2="cuto"
print(TipoRima(v1,v2))
print(ArchivoSalida("estrofas.txt"))



