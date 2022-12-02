from padre import Persona

class Docente(Persona):
    titulo                 =str
    edad                   = int
    experienciaProfesional = int
    experienciaDocente     = int
    
    def __init__(self, nombre, apellido, titulo, edad, experienciaProfesional, experienciaDocente):
        super().__init__(nombre, apellido)
        self.titulo                 =str
        self.edad                   = int
        self.experienciaProfesional = int
        self.experienciaDocente     = int
        
    def BienvenidaDocente(self):
        print("Estimando Docente: " + self.nombre, self.apellido + ". le damos la bienvendida al IST Yavirac " + "agradecemos contar con sus " + str(self.experienciaDocente + self.experienciaProfesional) + " años de experiencia")

docente1 = Docente("Dayana", "Tafur", "Desarrollador de Software", 24, 2, 1)
docente1.BienvenidaDocente()
    
        