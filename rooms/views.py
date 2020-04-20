from django.shortcuts import render
from . import models
from math import ceil

def all_rooms(request):
    page = int(request.GET.get('page', 1))
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_room = models.Room.objects.all()[offset: limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "rooms": all_room,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )