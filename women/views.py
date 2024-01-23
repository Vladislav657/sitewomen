from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

menu = ["Главная страница", "О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a, self.b = a, b


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'float': 28.56,
            'list': [1, 2, 'abc', True],
            'set': {2, 7, 3, 5, 9},
            'dict': {'key1': 'value1', 'key2': 'value2'},
            'object': MyClass(10, 20)
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Страница по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Страница по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return redirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}</p>")


def page_not_found(request, exception):
    return HttpResponse("<h1>Страница не найдена</h1>")
