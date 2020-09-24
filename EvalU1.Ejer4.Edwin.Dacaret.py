class problema:
    """Clase problema"""
    lista = [1, 2, 3, 4, 5]
    cantidad = len(lista)
    solicitudes = cantidad - 1
    x = 10
    print("")
    print("")
    print("")
    print("Localiza el error en el siguiente bloque de código:")
    print("-------------------------")
    print("|| lista = [1,2,3,4,5] ||")
    print("|| lista[10]           ||")
    print("-------------------------")
    print("Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la "
          "causa y/o solución.")
    print("")
    print("--------")
    print("SOLUCIÓN")
    print("--------")
    print("En el bloque de codigo mencionado la lista contiene", len(lista), "items.")
    print("Por lo tanto las solicitudes de intems validas en esa lista empiezan en 0 y llegan hasta", solicitudes, ".")

    def solucion(self):
        #print("--- metodo solucion ---")
        if self.x >= 5:
            self.x = self.x
            print("")
            print("Para solucionar el problema, si lista[x] recibe: ", self.x,".")
            print("Solicitamos ingresar un valor entre 0 y", str(self.solicitudes), ".")
            self.x = int(input('Ingresando: '))
            #print(self.x)
            obj.solucion()
        else:
            print("")
            print("ERROR SOLUCIONADO.")
            print("Fue ingresado valor ", self.x,)
            print("que es valido y traerá el ", self.x + 1, "° elemento de la lista.")

obj = problema()
obj.solucion()



