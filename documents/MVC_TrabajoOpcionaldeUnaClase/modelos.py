#####CASO DE USO --> PROPONER PLATO
class Plato:
    def __init__(self, nombre, precio, descripcion):
        #Cada plato solo tiene nombre, precio descripcion y las fotos
        self.nombre = nombre
        self.precio = precio


        self.descripcion = descripcion
        self.fotos = []


    #Metodo sencillo para cambiar el precio más adelante si se discute con el Cocinero
    def establecer_precio(self, nuevo_precio):

        self.precio = nuevo_precio

    #Añadir fotos poco a poco, Son las fotos de referencia del plato y son opcionales
    def anadir_foto(self, nombre_foto):


        self.fotos.append(nombre_foto)

    def __str__(self): #Para mostrar el plato:
        texto = self.nombre + " - " + str(self.precio) + " €\n"
        texto += "   Descripción: " + self.descripcion + "\n"

        
        texto += "   Fotos de Referencia: " + str(len(self.fotos))
        return texto
