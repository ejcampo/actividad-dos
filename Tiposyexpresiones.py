# Conversión de entero a decimal
entero = 10
decimal = float(entero)
print("Entero:", entero)
print("Decimal convertido:", decimal)
print ()

# Conversión de decimal a entero
decimal = 9.75
entero = int(decimal)
print("Decimal:", decimal)
print("Entero convertido:", entero)
print ()

# Conversión de cadena a entero
cadena = "123"
entero = int(cadena)
print("Cadena:", cadena)
print("Entero convertido:", entero)
print ()

#Multilineas de cadenas
texto_multilinea = '''Este 
texto ocupa
varias líneas.'''
print(texto_multilinea)
print ()

#Funcion len()
cadena = "Popayan"
longitud = len(cadena)
print("La longitud de la cadena es:", longitud)
print ()

# Obtener los primeros 3 caracteres de una cadena
cadena = "Cajibio"
primeros_3 = cadena[:3]
print("Primeros 3 caracteres:", primeros_3)
print ()

# Obtener los caracteres de en medio de una cadena
cadena = "Cajibio"
medio = cadena[2:4]
print("Caracteres del medio:", medio)
print ()

# Obtener los ultimos 3 caracteres de una cadena
cadena = "Cajibio"
ultimos_3 = cadena[-3:]
print("Últimos 3 caracteres:", ultimos_3)
print ()

# Función upper() para convertir a mayúsculas
cadena = "bogota"
mayusculas = cadena.upper()
print("Cadena en mayúsculas:", mayusculas)
print ()

# Función lower() paraConvertir a minúsculas
cadena = "BOGOTA"
minusculas = cadena.lower()
print("Cadena en minúsculas:", minusculas)
print ()

#Multilineas de cadenas de caracteres
texto_multilinea = '''Este otro
texto tambien ocupa
varias líneas.'''
print(texto_multilinea)
print ()

# Función strip() para
# eliminar espacios al inicio y al final
cadena_con_espacios = "   Cali es Cali   "
sin_espacios = cadena_con_espacios.strip()
print("Cadena sin espacios:", sin_espacios)
print ()

# Función replace() para reemplazar palabras
cadena = "Hola cali"
nueva_cadena = cadena.replace("cali", "ciudad bella")
print("Cadena modificada:", nueva_cadena)
print ()

# Función split() para separar por espacios
cadena = "Popayan ciudad blanca"
palabras = cadena.split()
print("Palabras separadas:", palabras)
print ()

# Formato de cadenas F-String
nombre = "Julian"
edad = 22
mensaje = f"Me llamo {nombre} y tengo {edad} años."
print(mensaje)
