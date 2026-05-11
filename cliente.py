from excepciones import ErrorValidacion

class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = None
        self.__email = None

        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        if not nombre or len(nombre) < 3:
            raise ErrorValidacion("Nombre inválido")
        self.__nombre = nombre

    def set_email(self, email):
        if "@" not in email:
            raise ErrorValidacion("Email inválido")
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"{self.__nombre} - {self.__email}"
