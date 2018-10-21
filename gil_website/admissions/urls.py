from django.urls import path
from . import views


app_name = "admissions"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('zhenshi', views.ZhenshiView.as_view(), name='zhenshi'),
    path('MaDegreeRequirements', views.MADegreeRequirements.as_view(), name='ma_degree'),

]
