from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.EventListView.as_view(), name='index'),
]