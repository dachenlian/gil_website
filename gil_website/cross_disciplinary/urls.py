from django.urls import path
from . import views

app_name = "cross"

urlpatterns = [
    path("index", views.IndexView.as_view(), name='index'),
    path("purpose", views.PurposeView.as_view(), name='purpose'),
    path("requirements", views.RequirementsView.as_view(), name='requirements'),
    path("course_info", views.CourseInfoView.as_view(), name='course_info'),
    path("student", views.StudentAreaView.as_view(), name='student'),
    path("student/signup", views.SignUpView.as_view(), name='signup'),
    path("profile/<int:pk>/", views.ProfileDetailView.as_view(), name='profile_detail'),
    path("profile/<int:pk>/update", views.ProfileUpdateView.as_view(), name='profile_update'),
]
