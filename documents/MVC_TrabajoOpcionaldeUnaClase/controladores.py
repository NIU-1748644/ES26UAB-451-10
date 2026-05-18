#####CASO DE USO --> PROPONER PLATO

from modelos import Plato

from vistas import VistaPlato #Importamos vistas y modelos

class ControladorPlato:
    def __init__(self):
        self.vista = VistaPlato()


        self.lista_platos = []

    def proponer_plato(self):
        #Pedimos los datos para crear el plato primero
        nombre, precio, descripcion = self.vista.pedir_datos_plato()
        
        #Creamos el objeto Plato --> el Modelo
        nuevo_plato = Plato(nombre, precio, descripcion)
        
        #Aqui damos la opcion de cambiar el precio de forma opcional por si se ha discutido con el cocinero
        if self.vista.preguntar_cambiar_precio() == "si":
            nuevo_precio = self.vista.pedir_nuevo_precio()
            nuevo_plato.establecer_precio(nuevo_precio)

            #Avisamos por pantalla del cambio
            self.vista.mostrar_mensaje("Precio actualizado a " + str(nuevo_precio) + " €.")
        
        #Por ultimo --> bucle para añadir fotos
        while True:
            foto = self.vista.pedir_foto()
            if foto == "":  #Si no hay ninguna foto salimos
                break

            
            nuevo_plato.anadir_foto(foto)
        
        #Para guardar en la lista global hacemos:
        self.lista_platos.append(nuevo_plato)
        self.vista.mostrar_mensaje("Plato guardado con éxito!")

    def ver_lista_platos(self):
        self.vista.mostrar_menu(self.lista_platos) #Para enseñar todos los platos
