from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import *
from datetime import datetime

clientes = []
reservas = []

def log_error(msg):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def crear_cliente():
    try:
        nombre = input("Nombre: ")
        email = input("Email: ")
        cliente = Cliente(nombre, email)
        clientes.append(cliente)
        print("✅ Cliente creado")
    except Exception as e:
        log_error(str(e))
        print("❌ Error:", e)

def crear_reserva():
    try:
        if not clientes:
            raise ErrorReserva("No hay clientes registrados")

        for i, c in enumerate(clientes):
            print(i, "-", c)

        idx = int(input("Seleccione cliente: "))
        cliente = clientes[idx]

        print("1. Sala\n2. Equipo\n3. Asesoría")
        tipo = int(input("Seleccione servicio: "))

        if tipo == 1:
            servicio = ReservaSala("Sala", 100)
            horas = int(input("Horas: "))
            costo = servicio.calcular_costo(horas)

        elif tipo == 2:
            servicio = AlquilerEquipo("Equipo", 50)
            dias = int(input("Días: "))
            costo = servicio.calcular_costo(dias)

        elif tipo == 3:
            servicio = Asesoria("Asesoría", 200)
            nivel = input("Nivel (basico/avanzado): ")
            costo = servicio.calcular_costo(nivel)

        else:
            raise ErrorServicio("Tipo inválido")

        reserva = Reserva(cliente, servicio)
        pago = reserva.procesar_pago()
        reserva.confirmar()

        reservas.append(reserva)

        print("✅ Reserva creada. Costo:", costo)

    except Exception as e:
        log_error(str(e))
        print("❌ Error:", e)

def ver_reservas():
    for r in reservas:
        print(r.cliente, "-", r.estado)

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Crear cliente")
        print("2. Crear reserva")
        print("3. Ver reservas")
        print("4. Salir")

        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            crear_reserva()
        elif op == "3":
            ver_reservas()
        elif op == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

menu()