class Mago:

    #Metodo Especial: CONSTRUCTOR
    def __init__(self, nombre, hechizos=None):
        self.nombre = nombre
        self.hechizos = hechizos if hechizos else []

    #Metodo Especial: TO STRING (se identifica con una cadena de caracteres la instancia)
    def __str__(self):
        return f"Hola! Mi nombre es {self.nombre}, el mago"
    
    #Metodo Especial: LENGHT
    def __len__(self):
        return len(self.hechizos)
    
    #Metodo Especial: EQ
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos
    
    #Metodo Especial: ADD
    def __add__(self, otro):
        if isinstance(otro, Mago):
            return Mago(f"{self.nombre}-{otro.nombre}")
        else:
            raise TypeError("Solo puedes combinar dos Magos")