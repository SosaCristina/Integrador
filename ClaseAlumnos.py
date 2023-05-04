
class Alumno:
    __dni=""
    __apellido=""
    __nombre=""
    __carrera=""
    __año_cursa=int

    def __init__(self,doc,a,n,c,año):
        self.__dni=doc
        self.__apellido=a
        self.__nombre=n
        self.__carrera=c
        self.__año_cursa=año
        
    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getaño(self):
        return self.__año_cursa
    def __str__(self):
        return 'DNI:{} - NOMBRE Y APELLIDO:{} {} - CARRERA:{} - AÑO QUE CURSA:{}'.format(self.__dni,self.__nombre,self.__apellido,self.__carrera,self.__año_cursa)
    
    
    def __gt__(self,otro):
        primero=str(self.__año_cursa)+self.__apellido+self.__nombre
        segundo=str(otro.__año_cursa)+otro.__apellido+otro.__nombre
        return primero > segundo