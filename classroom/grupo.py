from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12" # None

    def __init__(self, grupo = "grupo predeterminado" , asignaturas = [], estudiantes = []): # Constructor /grupo ordinario
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):#kwargs
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    #def agregarAlumno(self, alumno, lista = []): #lista = []
    #    #print(lista)
    #    lista.append(alumno)
    #    self.listadoAlumnos = self.listadoAlumnos + lista

    def agregarAlumno(self, alumno, lista = None):
        if lista is None:
            lista = []
        lista.append(alumno)
        #print(lista)
        self.listadoAlumnos = self.listadoAlumnos + lista
    
    def __str__(self):
        cadena = "Grupo de estudiantes: "+self._grupo
        return cadena

    # def __str__(self):
    #     pass

   # @ classmethod
   # def asignarNombre(cls, nombre="Grado 12"): #Grado 10
   #     cls.grado = nombre
   
   # @ classmethod
   # def asignarNombre(cls, nombre="Grado 4"): #Grado 6
   #     cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"): #Grado 4
        cls.grado = nombre

if __name__ == "__main__":
    grupo = Grupo()
    print(grupo)