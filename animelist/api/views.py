from django.shortcuts import render

from django.http import JsonResponse

def user_profile(request):
    data = {
        "username": "fellowweeb",
        "email": "fellow-weeb@animu.ru",
        "bio": "Anime weaboo"
    }
    return JsonResponse(data)

def anime_list(request):
    data = [
        {"id": 1, "title": "Attack on Titan", "category": "Action"},
        {"id": 2, "title": "Death Note", "category": "Detective"},
        {"id": 3, "title": "One Punch Man", "category": "Comedy"},
    ]
    return JsonResponse({"animes": data})

def category(request, category_name):
    data = {
        "category": category_name,
        "description": f"Description for the {category_name} category.",
    }
    return JsonResponse(data)

# Create your views here.
