class Extraterrestre:
    """Clase Extraterrestre"""
    print("")
    print("")
    planeta = input("Defina origen del alien: ").upper()
    comidaFavorita = input("Defina comida Favorita: ").upper()
    hostil = False

    def alimentar(self):
        print("")
        comida = input('Escriba una comida para ofrecer al alien: ').upper()
        self.comida = comida
        #print("--- metodo alimentar ---")
        #print("   input alimentar recibe: " + comida)
        #print("self.comida recibe comida: " + comida)
        #print("here starts an if: self.comida == self.comidaFavorita then hostil keep false")
        #print("")

        if self.comida == self.comidaFavorita:
            self.hostil = bool(False)

            if self.hostil == False:
                print("")
                print(">>> Extraterrestre de planeta " + self.planeta + " contento")
                #print('Comida Favorita es: ' + self.comidaFavorita)
                #print('      Alien recibe: ' + self.comida)
                #print("   hostil mantiene: " + str(self.hostil))

            else:
                self.hostil = bool(True)
        else:
            print("")
            print(">>> Extraterrestre de " + self.planeta + " enojado.")
            #print('Comida Favorita es: ' + self.comidaFavorita)
            #print('      Alien recibe: ' + self.comida)
            #print("     Hostil recibe: " + str(self.hostil))
            #print(bool(hostil))

alien = Extraterrestre()
alien.alimentar()
"""print("-------")
print("Origen recibe: " + alien.planeta)
print("Favorita recibe: " + alien.comidaFavorita)
print("Hostil recibe: " + str(alien.hostil))
print("-------")
print("")"""

