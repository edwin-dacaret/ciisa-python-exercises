class CuentaCorriente:

    def __init__(self, titular=None, numero=0, saldo=0.0):
        self.titular = titular if not titular else titular
        self.numero = numero if not numero else numero
        self.saldo = saldo if not saldo else saldo

        # valida parametro titular obligatorio
        if not self.titular:
            print("PARÁMETRO TITULAR es OBLIGATORIO, favor inserir parametro.")
            return
        if self.titular != str(titular):
            print("PARÁMETRO TITULAR debe ser cadena de texto (str)")
            return
        else:
            self.titular = titular

        # valida parametro numero obligatorio
        if self.numero == 0:
            print("PARÁMETRO NÚMERO es OBLIGATORIO, favor inserir parametro.")
            return
        if self.numero == str(numero):
            print("PARÁMETRO NÚMERO debe ser de tipo entero (int)")
            return
        if self.numero != int(numero):
            print("PARÁMETRO NÚMERO debe ser de tipo entero (int)")
            return
        else:
            self.numero = numero

    def abonar(self, canAbo=0.0):
        self.canAbo = canAbo if not canAbo else canAbo
        if self.canAbo == None:
            print("Valor de abono NULL")
            self.canAbo = 0.0
            self.saldo = self.saldo
        if self.canAbo <= 0.0:
            self.saldo = self.saldo
            print("Metodo abono recibio parametro NEGATIVO o NULL")
            print("Saldo mantiene: ", str(self.saldo))
            return
        else:
            self.saldo = self.saldo + self.canAbo
            print("Cantidad abonada: " + str(self.canAbo))
            print("Saldo: " + str(self.saldo))

    def cargar(self, canCar=0):
        self.canCar = canCar if not canCar else canCar
        if self.canCar == None:
            print("Valor de cargo NULL")
            self.canCar = 0.0
            self.saldo = self.saldo
        if self.canCar < 0:
            print("Metodo cargar recibio parametro NEGATIVO")
            print("Saldo mantiene: ", str(self.saldo))
            return
        if self.canCar > self.saldo:
            self.saldo = 0
            print("Saldo: ", str(self.saldo), "porque cargo es mayor que saldo")
            return
        else:
            self.saldo = self.saldo - self.canCar
            print("Cantidad cargada: " + str(self.canCar))
            print("Saldo: " + str(self.saldo))


obj1 = CuentaCorriente("Nombre Titular", 699696)
print("REQ05 - 1. Abono y Cargo POSITIVOS:")
obj1.abonar(60)
print("-")
obj1.cargar(50)
print("")

obj2 = CuentaCorriente("Segundo Nombre Titular", 5, 100)
print("REQ05 - 2. Abono y Cargo NEGATIVOS:")
obj2.abonar(-50)
print("-")
obj2.cargar(-50)
print("-")
obj2.cargar(150)
print("")

obj3 = CuentaCorriente("Tercer Nombre Titular", 2332, 500)
print("REQ05 - 3. Abono y Cargo NULL:")
obj3.abonar(None)
print("-")
obj3.cargar(None)
print("")

obj4 = CuentaCorriente("Cuarto Nombre Titular", 8686868)
print("REQ05 - 4. Instanciación de clase CuentaCorriente solo con PARAMETROS OBLIGATORIOS:")
print(obj4.titular)
print(obj4.numero)
print(obj4.saldo)
print("")

obj5 = CuentaCorriente("Quinto Nombre Titular", 111, 65.231)
print("REQ05 - 5. Instanciación de clase CuentaCorriente con TODOS los PARAMETROS:")
print(obj5.titular)
print(obj5.numero)
print(obj5.saldo)






