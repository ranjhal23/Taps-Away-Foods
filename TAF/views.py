from django.shortcuts import render
from items.models import cuisines


def home(request):
    return render(request, 'index.html')


def auth(request):
    return render(request, 'TAFlog.html')


def cuisine(request, val):
    cuisses = cuisines.objects.all()
    con = {'val': val, 'cuisses': cuisses}
    return render(request, 'cuis.html', con)
