# from django.http import HttpResponse
from django.shortcuts import render

# Create Your Views Here

rooms = [
        {'id':1,'name':'Lets Learn Python'},
        {'id':2,'name':'Design With Me'},
        {'id':3,'name':'Frontend Developers'},
]

def home(request):
        context = {'rooms':rooms}
        return render(request, 'base/home.html', context)

def room(request, pk):
        room = None
        for i in rooms:
                if str(i['id']) == str(pk):
                        room = i
                        break
        context = {'room':room}

        return render(request, 'base/room.html', context)