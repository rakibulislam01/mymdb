from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
]
