from ClaseMaterias import Materias
import csv


class Manejador_M:
    __manejadorM=[]
    def __init__(self):
        self.__manejadorM=[]


    def agregar (self, unaMateria):
        self.__manejadorM.append(unaMateria)
        
    
    def crear_Materia(self):
        archivo=open("C:\\Users\\chili\\POO archivos\\materiasAprobadas.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                "Saltear cabecera"
                bandera= not bandera
            else:
                doc=fila[0]
                nombre_m=fila[1]
                fecha=fila[2]
                nota=fila[3]
                aprobacion=fila[4]
                unaMateria=Materias(doc,nombre_m,fecha,nota,aprobacion)
                self.agregar(unaMateria)
        archivo.close       

    def __str__(self):
        s=""
        for listaM in self.__manejadorM:
            s += str(listaM) + '\n'
        return s
    
    
    def promedio(self,d):
        p=0
        suma=0
        for alu in self.__manejadorM:
            if  alu.getdoc()==d:
                p+=1
                suma+=int(alu.getnota())
        total=float(suma/p)
        return total
    
    def informar(self,m,unAlumno):
        
        for lista in self.__manejadorM:
            if (m==lista.getmateria() and (lista.getaprobacion()=="P")):
                d=lista.getdoc()
                
                i=unAlumno.Buscar_DNI(d)  
                elAlumno=unAlumno.getAlumnoPorIndice(i)
                print("  DNI   -   APELLIDO Y NOMBRE   -   FECHA   -   NOTA   -   AÑO QUE CURSA")
                print("  {}    -     {} {}    -   {}   -   {} ".format(lista.getdoc(),elAlumno.getapellido(),elAlumno.getnombre(),lista.getfecha(),elAlumno.getaño()))
                


      
    


