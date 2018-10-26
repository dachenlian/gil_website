from django.views.generic.list import ListView
from .models import Event


class HomeListView(ListView):
    model = Event

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Event.objects.filter(type_of_event='NEWS')[:5]
        context['talks'] = Event.objects.filter(type_of_event='TALKS_EVENTS')[:5]
        return context

    template_name = 'homepage/index.html'


class EventListView(ListView):
    model = Event
    paginate_by = 100
    context_object_name = 'events'
    template_name = 'homepage/events_listview.html'
