#Django
from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    edad = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.nombre+' '+self.apellido
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Course(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Cualification(models.Model):
    estudiante = models.ForeignKey(Student, on_delete=models.PROTECT)
    curso = models.ForeignKey(Course, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=2, decimal_places=1)
    nota2 = models.DecimalField(max_digits=2, decimal_places=1)
    nota3 = models.DecimalField(max_digits=2, decimal_places=1)
    nota4 = models.DecimalField(max_digits=2, decimal_places=1)
    promedio = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.estudiante.nombre
    
    class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        promedio = ((nota1+nota2+nota3+nota4)/4)
        return promedio



class Period(models.Model):
    periodo1 = models.CharField(max_length=50)
    periodo2 = models.CharField(max_length=50)
    periodo3 = models.CharField(max_length=50)
    periodo4 = models.CharField(max_length=50)
    note_anual = models.CharField(max_length=50)

    def __str__(self):
        return self.note_anual

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'