from django.urls import path
from . import views

app_name = "cross"

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("purpose", views.PurposeView.as_view(), name='purpose'),
    path("requirements", views.RequirementsView.as_view(), name='requirements'),
    path("course_info", views.CourseInfoView.as_view(), name='course_info'),
    path("student", views.StudentAreaView.as_view(), name='student'),
]
