from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64


def home(request):
    # return HttpResponse('<h1>Welcome to Home Page </h1>')
    # return render(request,'home.html')
    #return render(request,'home.html',{'name':' Sahian Salomé Gutiérrez Ossa'})
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
         movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()
    return render(request,'home.html',{'name':' Sahian Salomé Gutiérrez Ossa','searchTerm':searchTerm, 'movies':movies})

def about(request):
     #return HttpResponse('<h1>Welcome to About page </h1>')
     return render(request,'about.html')

def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})

def statistic_views(request):
    matplotlib.use('Agg')

    # Obtener todas las películas
    all_movies = Movie.objects.all()

    movie_counts_by_year = {}
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

  
    plt.figure(figsize=(8, 5))
    bar_positions = range(len(movie_counts_by_year))
    plt.bar(bar_positions, movie_counts_by_year.values(), width=0.5, align='center')
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    image_png = buffer.getvalue()
    buffer.close()
    graphic_years = base64.b64encode(image_png).decode('utf-8')

    movie_counts_by_genre = {}
    for movie in all_movies:
        if movie.genre: 
            first_genre = movie.genre.split(",")[0].strip().capitalize() 
        else:
            first_genre = "None"
        if first_genre in movie_counts_by_genre:
            movie_counts_by_genre[first_genre] += 1
        else:
            movie_counts_by_genre[first_genre] = 1


    plt.figure(figsize=(8, 5))
    bar_positions = range(len(movie_counts_by_genre))
    plt.bar(bar_positions, movie_counts_by_genre.values(), width=0.5, align='center')
    plt.title('Movies per Genre (First Genre Only)')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, movie_counts_by_genre.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    image_png = buffer.getvalue()
    buffer.close()
    graphic_genres = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'statistics.html', {
        'graphic_years': graphic_years,
        'graphic_genres': graphic_genres
    })


    