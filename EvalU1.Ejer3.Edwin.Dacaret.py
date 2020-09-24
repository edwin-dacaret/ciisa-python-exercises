class Extraterrestre:
    """Clase Extraterrestre"""
    print("")
    print("")
    planeta = input("Defina origen del Alien: ").upper()
    comidaFavorita = input("Defina comida Favorita del Alien: ").upper()
    hostil = False

    def alimentar(self):
        print("")
        #print("--- METODO ALIMENTAR  ---")
        comida = input('Escriba una comida para ofrecer al Alien: ').upper()
        self.comida = comida
        if self.comida == self.comidaFavorita:
            self.hostil = bool(False)
            #print('Comida Favorita es: ' + self.comidaFavorita)
            #print('      Alien recibe: ' + self.comida)
            #print("   hostil recibe: " + str(self.hostil))
            print("")
            print(">>> Extraterrestre del planeta " + self.planeta + " contento")
            alien.invadir()
        else:
            self.hostil = bool(True)
            #print('Comida Favorita es: ' + self.comidaFavorita)
            #print('      Alien recibe: ' + self.comida)
            #print("     Hostil recibe: " + str(self.hostil))
            #print(bool(hostil))
            print("")
            print(">>> Extraterrestre del planeta " + self.planeta + " enojado.")
            alien.invadir()

    def invadir(self):
        #print("--- METODO INVADIR ---")
        if self.hostil == False:
            #print("Hostil tiene: " + str(self.hostil))
            print(">>> Extraterrestre del planeta " + self.planeta + " está muy satisfecho como para invadir su "
                                                         "planeta. Siga alimentándolo con " + self.comidaFavorita)
        else:
            #print("Hostil tiene: " + str(self.hostil))
            print(">>> Extraterrestre del planeta " + self.planeta + " invadirá su planeta si no le da " +
                  self.comidaFavorita)
            alien.alimentar()

alien = Extraterrestre()
alien.alimentar()

