from ClaseAlumnos import Alumno
import csv
import numpy as np

class Manejador_A:
   __cantidad=0
   __dimension=0
   __incremento=5
    
   def __init__(self, dimension, incremento=5):
     self.__alumnos=np.empty(dimension, dtype=Alumno)
     self.__cantidad=0
     self.__dimension=dimension
    
   def agregar (self,Alu):
     if self.__cantidad==self.__dimension:
          self.__dimension+=self.__incremento
          self.__alumnos.resize(self.__dimension)
     self.__alumnos[self.__cantidad]=Alu
     self.__cantidad+=1

   def crear_Alumno(self):
     archivo=open("C:\\Users\\chili\\POO archivos\\alumnos.csv")
     reader=csv.reader(archivo,delimiter=";")
     bandera=True
     for fila in reader:
          if bandera:
               "Saltear cabecera"
               bandera= not bandera
          else:
               dni=fila[0]
               apell=fila[1]
               nom=fila[2]
               carrera=fila[3]
               año_cursa=fila[4]
               Alu=Alumno(dni,apell,nom,carrera,año_cursa)
               self.agregar(Alu)
               
     archivo.close
    
   def mostrar (self):
       for a in self.__alumnos:
          print(a)

   def __str__(self):
     s=""
     for listaA in range(self.__cantidad):
          s+= str(listaA) + '\n'
     return s
    
    
    



   def ordenar (self):
       intercambio=True
       while intercambio:
          intercambio=False
          for i in range(len(self.__alumnos)-1):
             if(self.__alumnos[i]>self.__alumnos[i+1]):
                #SE PRODUCE EL INTERCAMBIO
                self.__alumnos[i],self.__alumnos[i+1]=self.__alumnos[i+1],self.__alumnos[i]
                #CAMBIA A TRUE LA VARIABLE PORQUE HUBO UN INTERCAMBIO
                intercambio=True
    
   def Buscar_DNI(self,d):
      
      valorretornar=None
      bandera=False
      indice=0
      while (indice<len(self.__alumnos) and not bandera):
         if (d== self.__alumnos[indice].getdni()):
            valorretornar=indice
            bandera=True
         else:
            indice+=1
      return valorretornar    

   def getAlumnoPorIndice(self, indice):
      return self.__alumnos[indice]
                 

       
        
        