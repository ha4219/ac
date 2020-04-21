from django.views.generic import ListView
from django.utils import timezone
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
