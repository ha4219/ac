from django.shortcuts import render
from . import models

def all_rooms(request):
    all_room = models.Room.objects.all()
    return render(request, 'rooms/home.html', context={'rooms': all_room})