from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.urls import reverse
from django_countries import countries
from django.shortcuts import render, redirect
# from django.http import Http404
from . import models, forms


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
    form = forms.SearchForm()
    return render(request, 'rooms/search.html', {'form': form})