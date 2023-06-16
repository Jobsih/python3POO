class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.set_edad(ed)
        self.__carrera = carr

    def set_nombre(self, nom):
        self.__nombre=nom
    def get_nombre(self):
        return self.__nombre

    def set_edad(self, ed):
        if ed >=8 and ed <=120:
            self.__edad=ed
        else:
            print("Esa edad no es válida")
            self.__edad=0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera=carr
    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "------------------- \n Nombre: "+self.__nombre
        cadena = cadena + "\n Edad: " +str(self.__edad)
        cadena = cadena + "\n Carrera: " +self.__carrera
        cadena = cadena + "\n-------------------"
        return cadena
    def estudiar(self, horas = 1):
        print(f"El alumn@ {self.__nombre} está estudiando por {horas} hora(s)")

class Perro:
    reino = "Canino"
    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura= estatura

    # Metodo de acceso get
    @property
    def raza(self):
        return self.__raza
    # Metodo de acceso set
    @raza.setter
    def raza(self, la_raza):
        self.__raza = la_raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, la_edad):
        if la_edad > 0 and la_edad < 20:
            self.__edad = la_edad
        else:
            print("Esa no es una edad valida")
            self.__edad = 0

    # Metodo de acceso get
    @property
    def estatura(self):
        return self.__estatura
    # Metodo de acceso set
    @estatura.setter
    def estatura(self, est):
        if est >0.1 and est < 1.1:
            self.__estatura = est
        else:
            print("No, bro")
            self.__estatura = 0.1
    def __str__(self):
        return f"""
        ___________________________
        | Raza: {self.__raza}     
        | Edad: {self.__edad}     
        | Estatura: {self.__estatura} 
        ---------------------------        
        """
    @staticmethod
    def es_cachorro(edad):
        return edad < 3
    @staticmethod
    def dormir(veces = 5):
        for n in range(veces):
            print(f"Dando vuelta { n + 1}")
        print("ZZZZZ")
    @classmethod
    def perro_grande(cls , est):
        if est > 0.79:
            return cls("",0,est)
            #Return Perro("",0,est)
    @classmethod
    def constructor_dos(cls, raz, ed):
        if ed > 0 and ed < 20:
            return cls(raz, ed , 0.0)
        else:
            return cls(raz,0,0)

