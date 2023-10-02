# _ Protected
# __ Private
class vehiculo:
    #Desde Aqui se incician los atributos de la clase
    __marca = '' # Privado
    __velocidad = 0 # Privad
    color = '' #Publico
    _pais = '' # Protegido
    _velocidad_max = 0
    #Metodos: Desde aqui se inician los metodos de la clase Vehiculo
    def setVelocidad(self, cant):
        self.__velocidad = self.__velocidad + cant
        if(self.__velocidad<0):
            self.__velocidad = 0
    def getVelocidad(self):
        return self.__velocidad 

def agregar_vehiculo ()->dict:
    vehiculos = {}
    obj = vehiculo
    nombre = input("Ingrese el nombre del vehiculo: ")
    vehiculos[nombre] = ""
    obj.__marca = input("Ingrese la marca del vehiculo: ")
    vehiculos[nombre] = obj
    return vehiculos

vehiculos = agregar_vehiculo()

print(vehiculos.items())