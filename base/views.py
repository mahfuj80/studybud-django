# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


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
        print(room.topic)
        context = {'room':room}
        return render(request, 'base/room.html', context)


def createRoom(request):
        form = RoomForm()
        if request.method == 'POST':
                print(request.POST)
                form = RoomForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('home')

        context = {'form':form}
        return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
        room = Room.objects.get(id=pk)
        form = RoomForm(instance=room)
        if request.method == 'POST':
                form = RoomForm(request.POST, instance=room)
                if form.is_valid():
                        form.save()
                        return redirect('home')

        context = {'form':form}
        return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
        room = Room.objects.get(id=pk)
        if request.method == 'POST':
                room.delete()
                return redirect('home')
        context = {'obj':room}
        return render(request, 'base/delete.html', context)