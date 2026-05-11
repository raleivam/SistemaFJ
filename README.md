# 🖥️ Sistema de Gestión Software FJ

Este proyecto consiste en un sistema desarrollado en Python que permite gestionar clientes, servicios y reservas sin el uso de bases de datos, aplicando principios de Programación Orientada a Objetos (POO) y manejo avanzado de excepciones.

---

## 🎯 Objetivo

Desarrollar una aplicación modular y funcional capaz de administrar operaciones de una empresa de servicios, garantizando estabilidad ante errores.

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Manejo de archivos (logs)
- Listas en memoria

---

## 🧱 Estructura del proyecto

SistemaFJ/
│── cliente.py
│── servicio.py
│── reserva.py
│── excepciones.py
│── main.py
│── logs.txt
│── README.md

## 🧠 Principios de POO aplicados

- **Encapsulación**: Protección de datos en la clase Cliente
- **Herencia**: Clases derivadas de Servicio
- **Polimorfismo**: Método `calcular_costo()` implementado de diferentes formas
- **Abstracción**: Clase abstracta Servicio

---

## 🔧 Funcionalidades

- Crear clientes
- Crear reservas
- Gestión de servicios
- Validación de datos
- Manejo de errores
- Registro de logs

---

## ⚠️ Manejo de errores

El sistema implementa:

- Excepciones personalizadas
- try / except / else / finally
- Registro de errores en archivo `logs.txt`

Esto permite que el sistema continúe funcionando ante fallos.

---

## ▶️ Ejecución del sistema

Para ejecutar el sistema:

```bash
python main.py

Autor
Andrés Leiva Medina
