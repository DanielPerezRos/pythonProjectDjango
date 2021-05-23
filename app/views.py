from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.shortcuts import render
import datetime
from .models import Book
from .models import Movie, Director, Direction, Genero, Biografia
from django.utils import timezone


# Create your views here.
def home_redirect(request):
    return HttpResponseRedirect("/movieslist")


def books(request):
    book1 = Book("Libro1")
    book2 = Book("Libro2")
    books = [book1, book2]

    data = {
        "books_list": books
    }
    return render(request, "books-list.html", context=data)


def hola_mundo(request):
    return HttpResponse("Hola mundo")


def adios_mundo(request):
    return HttpResponse("Adios mundo")


def hola_html(request):
    html = """
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">      
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/js/all.min.js" integrity="sha512-F5QTlBqZlvuBEs9LQPqc1iZv2UMxcVXezbHzomzS6Df4MZMClge/8+gXrKw2fl5ysdk4rWjR0vKS7NNkfymaBQ==" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css/main.css">
    <title>Prueba de vista Django</title>
</head>
<body>
<h1>hola html</h1>
</body>
</html>
    """
    return HttpResponse(html)


def adios_html(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">      
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/js/all.min.js" integrity="sha512-F5QTlBqZlvuBEs9LQPqc1iZv2UMxcVXezbHzomzS6Df4MZMClge/8+gXrKw2fl5ysdk4rWjR0vKS7NNkfymaBQ==" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css/main.css">
    <title>Prueba de vista Django</title>
</head>
<body>
<h1>Adios html</h1>
</body>
</html>
    """)


def home(request):
    return render(request, "home.html")


def contact(request):
    data = {
        "email": "ahhrrc@gmail.com",
        "current_year": datetime.date.today().year,
        "company_name": "Desarrollos cósmicos"
    }
    return render(request, "contact.html", context=data)


def welcome(request):
    return render(request, "layout/welcome.html")


def hola_mundo2(request):
    # return HttpResponse("Hola mundo")
    return render(request, "home.html")


def bye(request):
    data = {
        "mensaje": "Hasta luego desde templates de proyecto"
    }
    return render(request, "bye.html", context=data)


def hola_mundo_app(request):
    return render(request, "app.html")


def sintaxis(request):
    movie1 = Movie(1, "1234", "Titulo película1", 2001)
    movie2 = Movie(2, "1234", "Titulo película2", 1989)
    movie3 = Movie(3, "1234", "Titulo película3", 1979)
    movies = [movie1, movie2, movie3]

    data = {
        "movies": movies,
        "notification": "Cartelera Películas",
        "admin": False
    }

    return render(request, "sintaxis.html", context=data)


# ********************CRUD MOVIE*******************#


def movie_list(request):
    movies = Movie.objects.all()
    directores = Director.objects.all()

    print(type(movies))
    print(movies)
    data = {
        "movies": movies,
        "directores": directores,
        "notification": "Cartelera Películas",
        "admin": True
    }

    return render(request, "movie-list.html", context=data)


def load_movie(request, id):
    # carga los datos a actualizar en el formulario
    data = {
        "movie": Movie.objects.get(id=id),
        "generos": Genero.objects.all()
    }
    return render(request, "movie-edit.html", context=data)


def save_movie(request):
    # guarda los datos del formulario en base de datos
    if request.method == "GET":
        return render(request, "movie-edit.html")

    # Crear nueva pelicula
    if not request.POST.get("id"):
        movie = Movie.objects.create(
            isbn=request.POST.get("isbn"),
            title=request.POST.get("title"),
            year=int(request.POST.get("year")),
            published=bool(request.POST.get("published")),
            director=request.POST.get("director")
        )
        return HttpResponseRedirect("/app/movies/{}/get".format(movie.id))

    # Editar una película existente
    id_movie = int(request.POST.get("id"))
    movie = Movie.objects.get(id=id_movie)

    movie.isbn = request.POST.get("isbn")
    movie.title = request.POST.get("title")
    movie.year = int(request.POST.get("year"))
    movie.published = bool(request.POST.get("published"))
    movie.director = request.POST.get("director")

    movie.save()
    return HttpResponseRedirect("/app/movies/{}/get".format(id_movie))


def create_movie(request):
    movie_db = Movie.objects.create(isbn="12345asd", title="Pelicula CRUD", year=2021, published=True,
                                    director="Romero")

    director_db = Director.objects.create(
        first_name="Daniel",
        last_name="Fernández",
        email="daniel@mail.com",
        num_movies=19,
        creation_date=timezone.now(),
        married=True,
        salary=78000
    )
    print(movie_db)
    print(director_db)
    return HttpResponse("película y director creados")


def filter_movie(request, isbn):
    print(isbn)
    result = Movie.objects.filter(isbn=isbn)
    print(result)
    return HttpResponse(result)


def movie_director_filter(request):
    director_id_str = request.GET.get("director_id")
    director_id = int(director_id_str) if director_id_str else None
    if director_id:
        data = {
            "movies": Movie.objects.filter(director_id=director_id),
            "director": Director.objects.all(),
            "director_id": director_id
        }
        return render(request, "movie-list.html", context=data)
    return HttpResponseRedirect("/movieslist")


def get_movie(request, id):
    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "movie-view.html", context=data)


# def update_movie(request):
#     movie1 = Movie.objects.get(id=1)
#     movie1.title = "Los Pilares de la Tierra CRUD"
#     movie1.year = 1999
#
#     movie1.save()
#     return HttpResponse(movie1)


def delete_movie(request, pk):
    try:
        movie1 = Movie.objects.get(pk=pk)
        movie1.delete()
        return HttpResponseRedirect("/app/movieslist")
    except Movie.DoesnotExists:
        return HttpResponseNotFound("Película no encontrada")


def delete_movies_by_year(request, year):
    movies = Movie.objects.filter(year=year)
    result = movies.delete()
    return HttpResponse("{} Películas borradas correctamente".format(result[0]))


# ********************CRUD DIRECTOR*******************#

def director_list(request):
    data = {
        "directores": Director.objects.all()
    }

    return render(request, "director-list.html", context=data)


def director_get(request, id):
    data = {
        "director": Director.objects.get(id=id)
    }
    return render(request, "director-view.html", context=data)


def director_delete(request, pk):
    try:
        director1 = Director.objects.get(pk=pk)
        director1.delete()
        return HttpResponseRedirect("/app/directores")
    except Director.DoesnotExists:
        data = {
            "error": "Director no encontrado"
        }
        return render(request, "notfound-404.html", context=data)


def director_load(request, id):
    # carga los datos a actualizar en el formulario
    data = {
        "director": Director.objects.get(id=id),
        "directions": Direction.objects.all()
        # "directions": Direction.objects.exclude(director__isnull=False)
    }
    return render(request, "director-edit.html", context=data)


def director_save(request):
    # guarda los datos del formulario en base de datos
    if request.method == "GET":
        data = {
            "directions": Direction.objects.all()
            # "directions": Direction.objects.exclude(director__isnull=False)

        }
        return render(request, "director-edit.html", context=data)

    # Crear nuevo director
    if not request.POST.get("id"):
        direction_id_str = request.POST.get("direction_id")
        direction_id = int(direction_id_str) if direction_id_str else None

        # Extraer datos de la biografía
        year = int(request.POST.get("year")) if request.POST.get("year") else None
        description = request.POST.get("description")

        biografia = None
        if description and year:
            biografia = Biografia.objects.create(year=year, description=description)

        director = Director.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            num_movies=int(request.POST.get("num_movies")),
            creation_date=timezone.now(),
            married=bool(request.POST.get("married")),
            salary=float(request.POST.get("salary")),
            direction_id=direction_id,
            biografia_id=biografia.id if biografia else None
        )
        return HttpResponseRedirect("/app/directores/{}/get".format(director.id))

    # Editar una director existente

    # Extraer datos de la biografía
    year = int(request.POST.get("year")) if request.POST.get("year") else None
    description = request.POST.get("description")

    id_director = int(request.POST.get("id"))
    director = Director.objects.get(id=id_director)

    direction_id_str = request.POST.get("direction_id")
    direction_id = int(direction_id_str) if direction_id_str else None

    director.first_name = request.POST.get("first_name")
    director.last_name = request.POST.get("last_name")
    director.email = request.POST.get("email")
    director.num_movies = int(request.POST.get("num_movies"))
    director.married = bool(request.POST.get("married"))
    director.salary = float(request.POST.get("salary"))
    director.direction_id = direction_id  # se asocia la dirección

    if director.biografia_id:  # editar biografía
        director.biografia.year = year
        director.biografia.description = description
        director.biografia.save()
    elif description and year:  # crear biografía
        biografia = Biografia.objects.create(year=year, description=description)
        director.biografia_id = biografia_id

    director.save()
    return HttpResponseRedirect("/app/directores/{}/get".format(id_director))


def direction_delete(request, pk):
    try:
        direction = Direction.objects.get(pk=pk)
        direction.delete()
        return HttpResponseRedirect("/app/directores")
    except Direction.DoesnotExists:
        data = {
            "error": "Dirección no encontrada"
        }
        return render(request, "notfound-404.html", context=data)
