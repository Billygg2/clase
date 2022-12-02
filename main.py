class persona:
    nombre = str
    edad  = int
    
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
        
    def saluda(self, otra_persona):
     return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'
        
if __name__=="__main__":
    Persona1 = persona("Diego", 33)
    Persona2 = persona("Carla", 35)
    
    print (Persona1.saluda(Persona2))

class MiClase:
    nombre = "Diego"
    edad = 29
    
p1 = MiClase()
print(p1.nombre)

# la funcion __int__()

class Persona2:
    nombre = str
    edad = int
    genero = str
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

p2 = Persona2("Diego", 29, "Masculino")

print(p2.nombre)
print(p2.edad)
print(p2.genero)

#La funcion __str__()

class persona3:
    nombre   = str
    edad     = int
    genero   = str
    estatura = int
    
    def __init__(self, nombre, edad, genero, estatura):
        self.nombre   = nombre
        self.edad     = edad
        self.genero   = genero
        self.estatura = estatura
        
    def __str__(self):
        return f'Hola me llamo {self.nombre}' 
    
p3 = persona3("Juan", 21, "Masculino", 1.89)

print(p3)

# Metodos dentro de Objetos

class persona4:
    nombre   = str
    semestre = str
    
    def __init__(self, nombre, semestre):
        self.nombre   = nombre
        self.semestre = semestre
        
    def saludo(self):
        print("Bienvenido" + self.nombre + "al " + self.semestre)
         
p4 = persona4("Antonio", "Segundo")
p4.saludo()

p4.nombre = "Jonathan"
p4.saludo()

del p4.semestre
p4.saludo()

del p4
p3.saludo()