from cosas import Alumno, Perro

def main():
    al1 = Alumno('José',19,'ICO')
    print(vars(al1))
    al1.__nombre = 'Diego'
    print(vars(al1))
    al1.set_nombre('Maria')
    print(vars(al1))
    print('-----To String-----')
    print(al1)
    al1.estudiar()

    print('-------Perro-------')
    perro1 = Perro("Poodle",2, 0.35)
    print(vars(perro1))
    # Set en notacion Pythonic
    perro1.raza = "De la calle"
    print(vars(perro1))
    perro1.edad=12
    perro1.estatura= 0.42

    print(perro1.edad)
    cachorro = Perro.es_cachorro(int(perro1.edad))
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)

main()