from ClaseAlumnos import Alumno
from ClaseManejadorAlumnos import Manejador_A
from ClaseMaterias import Materias
from ClaseManejadorMaterias import Manejador_M

import csv

if __name__=="__main__":
    unAlumno=Manejador_A(3,5)
    unaMateria=Manejador_M()
    unAlumno.crear_Alumno()
    print("_______________ARREGLO DE ALUMNOS_______________")
    #unAlumno.mostrar()
    unaMateria.crear_Materia()
    print("_______________LISTA DE MATERIAS_______________")
    #print(unaMateria)

    opcion=0
    def menu():
        opc=int(input("Seleccionar una opcion \n"+
                      "1)Ingresar DNI de alumno para conocer promedio con aplazo y sin aplazo \n"+
                      "2)Ingresar Nombre de materia para conocer los estudiantes que la aprobaron en forma promocional\n"+
                      "3)Listado de alumnos ordenado: por el año que cursan y alfabéticamente por apellido y nombre\n"+
                      "4)finalizar\n"))
        return opc
    while opcion!=4:
        opcion=menu()
        if opcion==1:
            d=input("Ingresar documento del alumno:")
            prom=float(unaMateria.promedio(d))
            print("El promedio del alumno ingresado es:",prom)
        if opcion==2:
            m=input("Ingresar nombre de la materia:")
            unaMateria.informar(m,unAlumno)
               
        if opcion==3:
            unAlumno.ordenar()
            unAlumno.mostrar()




   