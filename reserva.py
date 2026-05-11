from excepciones import ErrorReserva

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    def confirmar(self):
        try:
            self.estado = "confirmada"
        except Exception as e:
            raise ErrorReserva("Error al confirmar") from e

    def cancelar(self):
        self.estado = "cancelada"

    def procesar_pago(self, *args):
        try:
            costo = self.servicio.calcular_costo(*args)
        except Exception as e:
            raise ErrorReserva("Error en cálculo") from e
        else:
            return costo
        finally:
            print("Intento de pago realizado")
