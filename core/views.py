from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'pagina principal',
        'content': 'Bem vindo a pagina principal'
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        'title': 'pagina sobre',
        'content': 'Bem-vindo a pagina sobre'
    }
    return render(request, 'about/view.html', context)


def contact_page(request):
    context = {
        'title': 'pagina de contato',
        'content': 'Bem-vindo a pagina de contato'
    }
    return render(request, 'contact/view.html', context)
