class Extraterrestre:
    """Clase Extraterrestre"""
    print("")
    print("")
    planeta = input("Defina origen del alien: ").upper()
    comidaFavorita = input("Defina comida Favorita: ").upper()
    hostil = False

alien = Extraterrestre()
print("")
print("Planeta recibe: " + alien.planeta)
print("Favorita recibe: " + alien.comidaFavorita)
print("Hostil recibe: " + str(alien.hostil))
