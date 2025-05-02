class X:
    def metodo(self):
        print("Método de X")

class Y:
    def metodo(self):
        print("Método de Y")

class Z(X, Y):
    def metodo(self):
        print("Método de Z")
        super().metodo()

z = Z()
z.metodo()

# Muestra cómo se resolverá la herencia
print(Z.__mro__)
