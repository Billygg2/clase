# Herencias

class Persona:
    nombre   = str
    apellido = str
    
    def __init__(self, nombre, apellido):
        self.nombre   = nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(self.nombre, self.apellido)
        
x = Persona("Alexander", "Flores")
x.imprimir()

# Herencia simple

class Studiante(Persona):
    pass

y = Studiante("Jerremi", "Cañizares")
y.imprimir()

# Agregar atributos a una Herencia

class Student(Persona):
    edad = int
    
    def __init__(self, nombre, apellido, edad):
        Persona.__init__(self, nombre, apellido)
        self.edad = edad

estudiante1 = Student("Carlos", "Dell", 30)
estudiante1.imprimir()

# Agragar metodos a una herencia

class Student1(Persona):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
        
    def bienvenido(self):
        print("Bienvenido " + self.apellido + " al " + self.semestre + " ingresas a los " + str(self.edad) + " años ")
        
pS = Student1("Diego" , "Yanez", 29, "Segundo")
pS.bienvenido()
        
