# from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create Your Views Here

rooms = [
        {'id':1,'name':'Lets Learn Python'},
        {'id':2,'name':'Design With Me'},
        {'id':3,'name':'Frontend Developers'},
]

def home(request):
        rooms = Room.objects.all()
        print(rooms)
        context = {'rooms':rooms}
        return render(request, 'base/home.html', context)

def room(request, pk):
        room = Room.objects.get(id=pk)
        context = {'room':room}
        return render(request, 'base/room.html', context)


