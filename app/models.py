from django.db import models
from django.utils import timezone


# Create your models here.
class Book:
    def __init__(self, title):
        self.title = title





class Direction(models.Model):
    street = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:  # Para cambiar el nombre a la tabla que se va a generar
        db_table = "directions"

    def __str__(self):
        return self.street + " - " + self.country


class Biografia(models.Model):
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(default=0, null=True, blank=True)

    class Meta:  # Para cambiar el nombre a la tabla que se va a generar
        db_table = "biografias"

    def __str__(self):
        return self.description

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False, default="email@mail.com")
    num_movies = models.IntegerField(default=1)
    creation_date = models.DateTimeField(default=timezone.now)
    married = models.BooleanField(default=False)
    salary = models.FloatField(default=0)

    direction = models.OneToOneField(Direction, on_delete=models.SET_NULL, null=True, blank=True) #ono to one
    biografia = models.OneToOneField(Biografia, on_delete=models.SET_NULL, null=True, blank=True) #ono to one

    class Meta:  # Para cambiar el nombre a la tabla que se va a generar
        db_table = "directores"

    def __str__(self):
        return self.first_name + " - " + self.last_name


class Genero(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    class Meta:  # Para cambiar el nombre a la tabla que se va a generar
        db_table = "generos"

    def __str__(self):
        return self.name + " - " + self.color

# class Editorial(models.Model):
#     pass
#
#
# class Library(models.Model):
#     pass
#
#
# class LibraryAddress(models.Model):
#     pass


class Movie(models.Model):
    # atributos
    isbn = models.CharField(max_length=40)
    title = models.CharField(max_length=150)
    year = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    # relaciones
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True) # Many to one
    generos = models.ManyToManyField(Genero)


    class Meta:  # Para cambiar el nombre a la tabla que se va a generar
        db_table = "movies"

    def __str__(self):
        return self.isbn + " - " + self.title



