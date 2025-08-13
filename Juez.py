#Importacion Modulo
import re 


# Abrir el archivo en modo lectura
Estrofastxt = open("estrofas.txt", "r", encoding="utf-8")

# Leer todo el contenido
ContenidoEstrofas = Estrofastxt.read()

# Imprimir el contenido
print(ContenidoEstrofas)

# Cerrar el archivo para liberar recursos
Estrofastxt.close()
