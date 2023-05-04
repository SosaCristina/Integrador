
class Materias:
    __documento=""
    __nombre_materia=""
    __fecha=""
    __nota=int
    __aprobacion=""

    def __init__(self,d,n,f,nota,aprob):
        self.__documento=d
        self.__nombre_materia=n
        self.__fecha=f
        self.__nota=nota
        self.__aprobacion=aprob

    def getmateria(self):
        return self.__nombre_materia
    def getdoc(self):
        return self.__documento
    def getfecha(self):
        return self.__fecha
    def getnota(self):
        return self.__nota
    def getaprobacion(self):
        return self.__aprobacion
     
    def __str__(self):
        return 'DNI:{} - NOMBRE DE MATERIA:{} - FECHA:{} - NOTA:{}'.format(self.__documento,self.__nombre_materia,self.__fecha,self.__nota)
 
    