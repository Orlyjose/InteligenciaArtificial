

# def computerAreaSquare(side):
#     return side*side

# def computerAreaCircle(radius):
#     pi=3.1415
#     return pi*radius**2

# print (f"The area of an aquare with side 3cm is {computerAreaSquare(3)}")
# print(f"The area of a circle with a radius of 3 is{computerAreaCircle(3):.2f}")


# class Geometry:
#     pi = 3.1415

#     def __init__(self, side, radius):  # CORREGIDO: __init__
#         self.side = side
#         self.radius = radius
#         print("The object was created successfully!")  # CORREGIDO: ortografía

#     def area(self):
#         squareArea = self.side * self.side
#         circleArea = Geometry.pi * self.radius ** 2
#         return [squareArea, circleArea]

# # Crear objeto
# areaSquareCircle = Geometry(3, 3)

# def computerAreaSquare(side):
#     return side*side

# def computerAreaCircle(radius):
#     pi=3.1415
#     return pi*radius**2

# print (f"The area of an aquare with side 3cm is {computerAreaSquare(3)}")
# print(f"The area of a circle with a radius of 3 is{computerAreaCircle(3):.2f}")


# class Geometry:
#     pi = 3.1415

#     def __init__(self, side, radius):  # CORREGIDO: __init__
#         self.side = side
#         self.radius = radius
#         print("The object was created successfully!")  # CORREGIDO: ortografía

#     def area(self):
#         squareArea = self.side * self.side
#         circleArea = Geometry.pi * self.radius ** 2
#         return [squareArea, circleArea]

# # Crear objeto
# areaSquareCircle = Geometry(3, 3)

# # Obtener resultado del área
# result = areaSquareCircle.area()  # CORREGIDO: guardar el resultado

# # Imprimir resultado
# print(len(result))
# print(f'The areas of the square and circle are: {result[0]:.2f} and {result[1]:.2f}')

# class Rectangle:
#     def __init__(self, width, height):
#         """
#         Inicializa un nuevo objeto Rectangle con un ancho y una altura.
#         """
#         self.width = width
#         self.height = height

#     def area(self):
#         """
#         Calcula y retorna el área del rectángulo.
#         """
#         return self.width * self.height

# # Ejemplo de uso:
# rectangulo1 = Rectangle(5, 10)
# print(f"El ancho del rectángulo es: {rectangulo1.width}")
# print(f"La altura del rectángulo es: {rectangulo1.height}")
# print(f"El área del rectángulo es: {rectangulo1.area()}")

# rectangulo2 = Rectangle(3.5, 7)
# print(f"El área del segundo rectángulo es: {rectangulo2.area()}")

# print('--------------------------------------------------------')
# class RectangleGeometry:
#     def __init__(self, width, height):
#         """
#         Inicializa un nuevo objeto RectangleGeometry con un ancho y una altura.
#         """
#         self.width = width
#         self.height = height
#         print("El objeto Rectángulo fue creado exitosamente!")

#     def area(self):
#         """
#         Calcula y retorna el área del rectángulo.
#         """
#         rectangle_area = self.width * self.height
#         return rectangle_area

# # Crear objeto RectangleGeometry
# mi_rectangulo = RectangleGeometry(8, 5)

# # Obtener el área
# area_rectangulo = mi_rectangulo.area()

# # Imprimir el resultado
# print(f'El área del rectángulo es: {area_rectangulo:.2f}')


# # # Obtener resultado del área
# # result = areaSquareCircle.area()  # CORREGIDO: guardar el resultado

# # # Imprimir resultado
# # print(len(result))
# # print(f'The areas of the square and circle are: {result[0]:.2f} and {result[1]:.2f}')

# class Rectangle:
#     def __init__(self, width, height):
#         """
#         Inicializa un nuevo objeto Rectangle con un ancho y una altura.
#         """
#         self.width = width
#         self.height = height

#     def area(self):
#         """
#         Calcula y retorna el área del rectángulo.
#         """
#         return self.width * self.height

# # Ejemplo de uso:
# rectangulo1 = Rectangle(5, 10)
# print(f"El ancho del rectángulo es: {rectangulo1.width}")
# print(f"La altura del rectángulo es: {rectangulo1.height}")
# print(f"El área del rectángulo es: {rectangulo1.area()}")

# rectangulo2 = Rectangle(3.5, 7)
# print(f"El área del segundo rectángulo es: {rectangulo2.area()}")

# print('--------------------------------------------------------')
# class RectangleGeometry:
#     def __init__(self, width, height):
#         """
#         Inicializa un nuevo objeto RectangleGeometry con un ancho y una altura.
#         """
#         self.width = width
#         self.height = height
#         print("El objeto Rectángulo fue creado exitosamente!")

#     def area(self):
#         """
#         Calcula y retorna el área del rectángulo.
#         """
#         rectangle_area = self.width * self.height
#         return rectangle_area

# # Crear objeto RectangleGeometry
# mi_rectangulo = RectangleGeometry(8, 5)

# # Obtener el área
# area_rectangulo = mi_rectangulo.area()

# # Imprimir el resultado
# print(f'El área del rectángulo es: {area_rectangulo:.2f}')




print('STUDEN CLASS.......')


import statistics
class Student:
    def __init__(self,name, grades):
        self.name=name
        self.grades=grades

    def averge_grade(self):
        score=statistics.mean(self.grades)
        return score
        

OrlyStuden=Student('orly',[6,7,9,8,7])

KevinStuden=Student('orly',[8,7,6,9,7])

print(f'THE SCORE OF ORLY STUDENT IS:{OrlyStuden.averge_grade()}')
print(f'THE SCORE OF IS KEVIN STUDENT IS:{KevinStuden.averge_grade()}')



print('ok')