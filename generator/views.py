from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-/~}{][|?><'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    context = {
        'password': thepassword
    }
    return render(request, 'generator/password.html', context)


def about(request):
    return render(request, 'generator/about.html')
