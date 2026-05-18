#####CASO DE USO --> PROPONER PLATO
class VistaPlato: #Las vistas es el mas complejo, avisamos todo el rato al usuario de lo que esta pasando
    def pedir_datos_plato(self):
        print("--- PROPONER UN NUEVO PLATO ---")

        nombre = input("Cómo se llama el plato?") #Con input dejamos que el usuario nos de la informacion
        precio = input("Qué precio tiene?")


        descripcion = input("Añade una descripción:")
        return nombre, precio, descripcion #devolvemos esto para el controlador

    def preguntar_cambiar_precio(self): #Esto lo necesita el controlado, sideciden con el cocinero cambiar el precio
        respuesta = input("Quieres cambiar el precio de este plato? (si o no): ")

        return respuesta


    def pedir_nuevo_precio(self): #Si la respuesta es si pedimos un precio

        nuevo_precio = input("Introduce el nuevo precio: ")
        return nuevo_precio

    def pedir_foto(self): #pedir foto se necesita para el bucle
        print("Puedes añadir fotos al plato (Opcional)")
        foto = input("Escribe el nombre de la foto (por ejemplo: pizza.jpg) o pulsa INTRO para terminar:")
        return foto



    #Le pasamos por referencia la lista de todos los platos guardados.
    def mostrar_menu(self, platos): #mostrar menu es para enseñar todos los platos guardados.
        print("--- PLATOS PROPUESTOS ---")


        if len(platos) == 0:
            print("Todavía no hay ningún plato propuesto.")


        else:
            for i, plato in enumerate(platos): #enumerate para sacar el indice
                print(str(i + 1) + ". " + str(plato))

                

    def mostrar_mensaje(self, mensaje):
        print("-->" + mensaje)
