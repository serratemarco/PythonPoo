#Clases y Objetos

#Clase estudiante
class Estudiante:
    #Constructor
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        #Metodo estudiar
        
    def estudiar(self):
         print("Estudiando....")
        
        
    #Solicitud de datos para crear el objeto 
nombre = input("Digame su nombre: ")
edad = input("Digite su edad: ")
grado = input("Digite su grado: ")

    #Asignamos los datos para crear el objeto 
estudiante = Estudiante(nombre, edad, grado)
print(f""""
      Datos del Estudiante: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
    