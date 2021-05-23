from django.contrib import admin

# Register your models here.
from .models import Movie, Director, Direction

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Direction)
