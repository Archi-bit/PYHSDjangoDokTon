from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'texton': 'Хороший сайт'
    }

    return render(request, 'main/about.html', context)