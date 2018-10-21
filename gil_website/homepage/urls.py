from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('allevents', views.EventListView.as_view(), name='events'),
]