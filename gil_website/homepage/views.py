from django.views.generic.list import ListView
from .models import Event


class EventListView(ListView):
    model = Event

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Event.objects.filter(type_of_event='NEWS')
        context['talks'] = Event.objects.filter(type_of_event='TALKS_EVENTS')
        return context

    template_name = 'homepage/index.html'
