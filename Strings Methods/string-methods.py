
texto = "hola mundo"

texto2 = "HOLA MUNDO"

texto3 = "    texto con espacios    "

texto4 = "manzana, naranja, manzana"

print("capitalize:", texto.capitalize()) #convierte la primera letra en mayuscula (el resto en minuscula)
print("upper:", texto.upper()) #convierte el texto entero en mayusculas
print("lower:", texto2.lower()) #convierte el texto entero en minusculas
print("strip:", texto3.strip()) #elimina los espacios al comienzo y al final
print("replace:", texto3.replace("espacios","gracia")) #reemplaza una palabra con otra
print("split:", texto.split(" ")) #separar texto en items de una lista
print("join:", ",".join(texto2)) #junta los items de una lista en un string
print("find:", texto.find("mundo")) #muestra la posicion donde arranca el texto ingresado
print("startswith:", texto.startswith("hola")) #indica si comienza o no con la palabra ingresada
print("endswith:", texto.endswith("mundo")) #indica si finaliza o no con la palabra ingresada
print("isdigit:", texto.isdigit()) #indica si todos los caracteres son numeros o no (espacios no son numeros)
print("isalpha:", texto.isalpha()) #indica si todos los caracteres son letras o no (espacios no son letras)
print("isalnum:", texto.isalnum()) #indica si todos los caracteres son alfanumericos o no (espacios no son letras y numeros)
print("isspace:", texto.isspace()) #indica si el string solo está compuesto de espacios
print("count:", texto4.count("manzana")) #indica cuantas veces se repite la palabra ingresada
print("index:", texto.index("mundo")) #similar a find
print("rfind:", texto4.rfind("manzana")) #muestra la ultima posicion donde arranca el texto ingresado