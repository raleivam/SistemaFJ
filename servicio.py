from abc import ABC, abstractmethod
from excepciones import ErrorServicio

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

# Servicio 1
class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        if horas <= 0:
            raise ErrorServicio("Horas inválidas")
        return self.precio_base * horas

# Servicio 2
class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1):
        if dias <= 0:
            raise ErrorServicio("Días inválidos")
        return self.precio_base * dias

# Servicio 3
class Asesoria(Servicio):
    def calcular_costo(self, nivel="basico"):
        if nivel == "basico":
            return self.precio_base
        elif nivel == "avanzado":
            return self.precio_base * 2
        else:
            raise ErrorServicio("Nivel inválido")