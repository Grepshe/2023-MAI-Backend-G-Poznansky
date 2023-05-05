from django.contrib import admin
from .models import UserProfile, Category, Anime, Review

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Anime)
admin.site.register(Review)


# Register your models here.
