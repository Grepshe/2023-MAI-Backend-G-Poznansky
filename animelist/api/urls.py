from django.urls import path
from . import views
from django.contrib import admin
from .models import UserProfile, Category, Anime, Review

app_name = 'api'

urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
    path('anime_list/', views.anime_list, name='anime_list'),
    path('category/<str:category_name>/', views.category, name='category'),
]
