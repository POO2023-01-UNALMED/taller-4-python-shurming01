class Asignatura:
 
    def __init__(self, nombre, salon ="remoto"): # Constructor
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        cadena = self._nombre +" "+self._salon
        return cadena

    def setNombre(self, nombre):
        self._nombre = nombre

    def get_Nombre(self):
        return self._nombre

    def set_Salon(self, salon):
        self._salon = salon

    def get_Salon(self):
        return self._salon
    
    # def __str__(self):
    #     pass

if __name__ == "__main__":
    asignatura = Asignatura()
    print(asignatura)

    
   

        

