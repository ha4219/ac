from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.urls import reverse
from django_countries import countries
from django.shortcuts import render, redirect
# from django.http import Http404
from . import models


class HomeView(ListView):
    ''' HomeView Definition '''
    model = models.Room
    paginate_by = 10
    ordering = 'created'
    paginate_orphans = 5
    page_kwarg = 'page'
    context_object_name = 'rooms'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['now'] = now
        return context
    
    
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, 'rooms/detail.html', {'room':room})
#     except models.Room.DoesNotExist:
#         raise Http404()


class RoomDetailView(DetailView):
    ''' RoomDetailView Definition '''
    model = models.Room
    # pk_url_kwarg = 'photato'
    

def search(request):
    city = request.GET.get('city')
    city = str.capitalize(city)
    country = request.GET.get('country', 'KR')
    room_type = int(request.GET.get('room_type', 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    instant = request.GET.get("instant", False)
    s_facilities = request.GET.get("facilities")	    
    super_host = request.GET.get("super_host", False)
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }
    
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }
    return render(request, 'rooms/search.html', {**form, **choices})