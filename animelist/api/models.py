from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Anime(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    users = models.ManyToManyField(UserProfile, related_name='favorite_animes')

class Review(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()

# Create your models here.
