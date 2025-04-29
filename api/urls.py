from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    LoginView, LogoutView, AktorListAPiView, RegisterAuthorsSerializer, AktorDetailApiview, SutradaraListAPiView, SutradaraDetailApiview, GenreListAPiView, GenreDetailApiview, NegaraListAPiView, NegaraDetailApiview, BahasaListAPiView, BahasaDetailApiview, FilmListApiView, FilmDetailApiview, RatingListAPiView, RatingDetailApiview
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL patterns yang lain
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


app_name = 'api'
urlpatterns = [
    path('api/v1/login', LoginView.as_view()),
    path('api/v1/logout', LogoutView.as_view()),
    path('api/v1/register', RegisterAuthorsSerializer.as_view()),
    path('api/aktor', views.AktorListAPiView.as_view()),
    path('api/aktor/<int:id>', views.AktorDetailApiview.as_view()),
    path('api/sutradara', views.SutradaraListAPiView.as_view()),
    path('api/sutradara/<int:id>', views.SutradaraDetailApiview.as_view()),
    path('api/genre', views.GenreListAPiView.as_view()),
    path('api/genre/<int:id>', views.GenreDetailApiview.as_view()),
    path('api/negara', views.NegaraListAPiView.as_view()),
    path('api/negara/<int:id>', views.NegaraDetailApiview.as_view()),
    path('api/bahasa', views.BahasaListAPiView.as_view()),
    path('api/bahasa/<int:id>', views.BahasaDetailApiview.as_view()),
    path('api/film', views.FilmListApiView.as_view()),
    path('api/film/<int:id>', views.FilmDetailApiview.as_view()),
    path('api/rating', views.RatingListAPiView.as_view()),
    path('api/rating/<int:id>', views.RatingDetailApiview.as_view()),
]