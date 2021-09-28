from django.db import models
import datetime
# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField("los nombres del usuario",max_length=100)
    apellidos = models.CharField("los apellidos del usuario",max_length=100)
    autos = models.ManyToManyField('Auto', verbose_name="los carros del usuario")


ESTADO_VALORES=(
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
) #para guardar el estado en un solo caracter y obtener
#su valor mediante el metodo get_estado_display()

class Website(models.Model):
    nombre = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    fecha_publicacion = models.DateField()
    calificacion = models.IntegerField()
    estado = models.CharField(choices=ESTADO_VALORES, max_length=1) #choises para que haga uso de la tupla
    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE) #para que borre en cascada
    def fecha_igual_dia_actual(self):
        if self.fecha_publicacion == datetime.date.today():
            return "Tiene la fecha actual"
        else:
            return "No fue publicado en la fecha actual"

    #se llama sin parentesis
    @property
    def get_nombre_y_calificacion(self):
        resultado:str = f"Nombre: {self.nombre} \nCalificacion: {str(self.calificacion)} "
        return resultado

    
    def __str__(self) -> str:
        return self.nombre

    
    def save(self,*args, **kwargs):
        print('Se guardo el objeto')
        return super().save(*args,**kwargs)

    


class Auto(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
