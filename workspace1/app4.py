class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def printingMessage(self):
        return f'The maker is: {self.maker}, the model is: {self.model}'


class Car(Vehicle):  # Hereda de Vehicle
    def __init__(self, maker, model, doors):
        super().__init__(maker, model)
        self.doors = doors

    def infoPrinting(self):
        return f'The maker is: {self.maker}, the model is: {self.model}, the number of doors is:{self.doors}'


class Truck(Vehicle):  # Hereda de Vehicle
    def __init__(self, maker, model, weight):
        super().__init__(maker, model)
        self.weight = weight

    def infoPrinting(self):
        return f'The maker is: {self.maker}, the model is: {self.model}, the weight is: {self.weight}'


# Crear objetos
vehiculoObject = Vehicle('Generic', 'FT223')
carObject = Car('Toyota', 'Hilux', 4)
truckObject = Truck('Hino', 'HG', 12300)

# Mostrar mensajes
print(vehiculoObject.printingMessage())
print(carObject.infoPrinting())
print(truckObject.infoPrinting())
