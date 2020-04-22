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
    room_types = models.RoomType.objects.all()
    form = {'city': city, 's_room_type': room_type, 's_country': country}
    choices = {'countries': countries, 'room_types': room_types}
    return render(request, 'rooms/search.html', {**form, **choices})