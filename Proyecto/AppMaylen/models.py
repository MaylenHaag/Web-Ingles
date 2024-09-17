from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Curso (models.Model) :
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    horario = models.CharField(max_length=40)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return "{} | ID: {}".format(self.nombre, self.id)






    