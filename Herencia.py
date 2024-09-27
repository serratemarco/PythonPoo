#Clase Padre
class Persona:
  def __init__(self, name, age, nationality):
    self.name = name
    self.age = age
    self.nationality = nationality
    
  def hablar(self):
    print ("Hola, soy", self.name)  
    
    
    
#Clase herencia  simple 
#Puede usar los metodos de la clase padre y tambien reescribirlos, o tener metodos propios

class Empleado(Persona):
  def __init__(self, name, age, nationality , job, salary):
    super().__init__(name, age, nationality)
    #Atributos propios de la clase Empleado
    self.job = job
    self.salary = salary
    
class Estudiante(Persona):
  def __init__(self, name, age, nationality , grado, carrera):
    super().__init__(name, age, nationality)
    #Atributos propios de la clase Estudiante
    self.grado = grado
    self.carrera = carrera
            




marco = Empleado("marco", 29, "paraguayo", "Progrador", 1000)
juan = Estudiante("Marco", 29, "Paraguayo", "Programador", 1000, "5to año", "Lic. Informatica") 

marco.hablar()
juan.hablar()

print (marco.name, marco.age, marco.nationality, marco.job, marco.salary)
  

  
  
  