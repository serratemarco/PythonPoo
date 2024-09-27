class Celular:
#Metodo Constructor / _init_ es un metodo especial / self es una forma de hacer referencia así mismo
    def __init__(self, marca, modelo, camara):
      #Atributos de instancia
      self.marca = marca;
      self.modelo = modelo;
      self.camara = camara;
      #Metodos
    def llamar(self):
        print(f"Estas llamando desde tu: {self.modelo} ")
    def cortar(self):
        print(f"Vas a cortar la llamada desde tu: {self.modelo} ")
      #Creando Objetos / Intancia de una clase
celular1 = Celular("Sansung", "S23", "48MP")
celular2 = Celular("Iphone 15", "Iphone 15 ProMax", "500MP" )
#Imprimiendo objetos
print("El celular es 1: " + celular1.marca, celular1.modelo, celular1.camara )
print("El celular es 2: "+ celular2.marca, celular2.modelo, celular2.camara )
    #LLamando a un metodo
celular1.llamar()
celular1.cortar()
celular2.llamar()
celular2.cortar()

