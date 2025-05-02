class A:
    def saludar(self):
        print("Hola desde A")

class B:
    def saludar(self):
        print("Hola desde B")

class C(A, B):
    pass

c = C()
c.saludar()  # ¿Qué método se ejecuta?

# Mostrar el orden de resolución de métodos (MRO)
print(C.__mro__)
