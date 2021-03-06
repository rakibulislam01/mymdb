from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('movie/<int:movie_id>/vote', views.CreateVote.as_view(), name='create_vote'),
    path('movie/<int:movie_id>/vote/<int:pk>', views.UpdateVote.as_view(), name='update_vote'),
    path('movie/<int:movie_id>/image/upload', views.MovieImageUpload.as_view(), name='movie_image_upload'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('person/<int:pk>', views.PersonDetail.as_view(), name='person_detail'),
]
