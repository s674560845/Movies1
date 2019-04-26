from django.shortcuts import render
from Movie import getmovies
from Movie import models
from django.http import HttpResponse
# Create your views here.

def movieShow(request):
    aa,bb,cc,dd=getmovies.get_movies()
    movie_type=models.movieType.objects.all()
    for i in range(len(aa)):
        models.movieType.objects.create(id=i,title=aa[i],director=bb[i],img=cc[i],dec=dd[i])
    return render(request,"GetMovies.html",{'list':movie_type})



