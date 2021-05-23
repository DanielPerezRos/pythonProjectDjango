
from django.urls import path
from . import views

urlpatterns = [
    path('holamundo', views.hola_mundo),
    path('adiosmundo', views.adios_mundo),
    path('holahtml', views.hola_html),
    path('adioshtml', views.adios_html),
    path('plantilla1', views.home),
    path('plantilla2', views.contact),
    path('books', views.books),
    path('welcome', views.welcome),
    path('holamundo2', views.hola_mundo2),
    path('bye', views.bye),
    path('holamundo_app', views.hola_mundo_app),
    path('movies', views.sintaxis),


    path('', views.home_redirect),
    # CRUD movies
    path('movieslist', views.movie_list, name="movie_list"),
    path('movies/create', views.create_movie),
    path('movies/<str:isbn>/filter', views.filter_movie),
    path('movies/<int:id>/get', views.get_movie, name="movie_view"),
    path('movies/<int:pk>/delete', views.delete_movie, name="movie_delete"),
    path('movies/<int:year>/delete/all', views.delete_movies_by_year),
    path('movies/save', views.save_movie, name="book_save"),
    path('movies/<int:id>/load', views.load_movie, name="movie_load"),

    path('movieslist/directores/', views.movie_director_filter, name='movie_director_filter'),

    # CRUD directores
    path('directores', views.director_list, name="director_list"),
    path('directores/<int:id>/get', views.director_get, name="director_view"),
    path('directores/<int:pk>/delete', views.director_delete, name="director_delete"),
    path('directores/save', views.director_save, name="director_save"),
    path('directores/<int:id>/load', views.director_load, name="director_load"),

    # CRUD direcciones
    path('directions', views.direction_delete, name='direction_delete')
]