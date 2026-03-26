from Clases.Mago import Mago


Merlin = Mago("Merlin", ["Bola de Fuego", "Rayo"])
Gandalf = Mago("Gandalf", ["LLamar a las aguilas cuando termino la pelicula", "Bola de fuego"])
Copia_Gandalf = Mago("Gandalf", ["LLamar a las aguilas cuando termino la pelicula", "Bola de fuego"])

print(Merlin) # devuelve el metodo __str__ que habiamos generado
print(len(Merlin)) # devuelve el metodo __len__ que habiamos generado

print(Gandalf)
print(len(Gandalf))

print(Merlin == Gandalf)

print(Gandalf == Copia_Gandalf) # devuelve una comparacion usando los criterios definidos en el metodo __eq__

mago_combinado = Merlin + Gandalf
print(mago_combinado)