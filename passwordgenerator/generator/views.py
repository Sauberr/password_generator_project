from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qazxswedcvfrtgbnhyujmkiolp')

    if request.GET.get('uppercase'):
        characters.extend(list('QAZXSWEDCVFRTGBNHYUJMKIOLP'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_?/<>,.'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))


    length = int(request.GET.get('length', 6))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    if request.GET.get('name'):
        names = ["Love", "World", "Peace", "Sauberr", 'EugenOP', 'Grohot', 'Luntik', 'Awarew', 'Stypyk', 'Keeper',
                 'SwagerFeed', 'Poss', '3F', 'Smokzi']

        name = ''

        name += random.choice(names)

        return render(request, 'generator/passwordandname.html', {'password': thepassword, 'nickname': name})
    else:
        return render(request, 'generator/password.html', {'password': thepassword})



