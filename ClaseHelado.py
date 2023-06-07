class Helado:
    __gramos: str
    __precio: str
    __sabores: list

    def __init__(self, gramos, precio):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []

    def __str__(self):
        return f"{self.__gramos} gr, {self.__precio} $"

    def mostrarSabores(self):
        for sabor in self.__sabores:
            print(sabor)

    def getGramos(self):
        return self.__gramos

    def getPrecio(self):
        return self.__precio

    def getSabores(self):
        return self.__sabores

    def sabores(self, sabor):
        self.__sabores.append(sabor)