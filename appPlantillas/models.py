from django.db import models

# Create your models here.
class Persona(models.Model):
    
    rut = models.CharField(max_length = 10 )
    nombre = models.CharField(max_length = 50)
    
    def __str__(self):
        return "Cliente: %s nombre: %s " %(self.rut,self.nombre)

    
    def getNombre(self):
        return self.nombre
    
    def getRut(self):
        return self.rut
    
    def getRutFormato(self):
        if(len(self.rut)>8):
            return "%s.%s.%s-%s" %(self.rut[0:2],self.rut[2:5],self.rut[5:8],self.rut[8])
        else:
            return "%s.%s.%s-%s" %(self.rut[0:1],self.rut[1:4],self.rut[4:7],self.rut[7])
        
    def funcionEjemplo(self):
        return "Texto de ejemplo de una Funcion"
