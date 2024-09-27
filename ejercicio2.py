class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre;
        self.edad = edad;
        self.grado = grado;
    def estudiar(self):
        print(f"Estudiando...");
        
#pedimos que ingrese los datos al usuario
nombre = input("Ingrese su nombre: "),
edad = input("ingrese su edad: "),
grado = input("ingrese su grado: "),

#creamos el objeto
estudiante = Estudiante(nombre, edad, grado);
#IMprimimos el objeto
print(f"""
        DATOS DEL ESTUDIANTE:  \n\n
        nombre: {estudiante.nombre}\n,
        edad: {estudiante.edad}\n,
        grado: {estudiante.grado}\n
    """);
#metemos a un bucle
while True:
        estudiar = input();
        if(estudiar.lower() == "estudiar"):
            estudiante.estudiar()
