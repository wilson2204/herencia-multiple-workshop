class Usuario:
    def info(self):
        print("Usuario: perfil básico.")

class Notificador:
    def info(self):
        print("Enviando notificación al usuario...")

class Administrador(Usuario, Notificador):
    def ejecutar(self):
        print("Ejecutando acciones de administración.")

# Instanciamos un administrador
admin = Administrador()
admin.info()         # ¿Qué versión de info() se ejecuta?
admin.ejecutar()

# Mostramos el MRO (Method Resolution Order)
print(Administrador.__mro__)
