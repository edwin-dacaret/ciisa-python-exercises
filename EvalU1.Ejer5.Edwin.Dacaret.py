class laLista:
    """Clase laLista"""
    lista = ["apple", "banana", "cherry"]
    print("")
    print("")
    print("Realiza una función llamada agregar_una_vez (lista, elemento) que reciba una lista y un elemento.")
    print("La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento.")
    print("Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError,")
    print("que debes capturar y mostrar este mensaje en su lugar:")
    print(">>>")
    print("Error: Imposible añadir elementos duplicados => [elemento].")
    print("")
    print("---------")
    print("SOLUCIÓN:")
    print("---------")

    def agregar_una_vez(self):
        print("")
        print("Lista contiene:")
        print(self.lista)
        elemento = input("Añadir elemento no repetido al final de la lista. ( 'salir' para terminar la lista. ): ")
        if elemento == str("salir"):
            print("")
            print("---------------")
            print("Lista terminada!")
            print(self.lista)
        else:
            try:
                if elemento not in self.lista:
                    self.lista.append(elemento)
                    print(self.lista)
                    obj.agregar_una_vez()
                else:
                    raise ValueError
                    pass
            except ValueError:
                print("")
                print("Error: Imposible añadir elementos duplicados =>", elemento)
                obj.agregar_una_vez()


obj = laLista()
obj.agregar_una_vez()

