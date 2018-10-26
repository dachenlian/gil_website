from django.urls import path
from . import views


app_name = "admissions"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('zhenshi', views.MAZhenshiView.as_view(), name='zhenshi'),
    path('regular', views.MARegularView.as_view(), name='regular'),
    path('MaDegreeRequirements', views.MADegreeRequirements.as_view(), name='ma_degree'),
    path('PhDDegreeRequirements', views.PhDDegreeRequirements.as_view(), name='phd_degree')

]
