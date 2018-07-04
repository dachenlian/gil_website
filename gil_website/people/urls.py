from django.urls import path

from . import views

app_name = 'people'
urlpatterns = [

    path('ma_students/', views.MasterStudentListView.as_view(), name='master_student_list_view'),
    path('phd_students/', views.DoctorateStudentListView.as_view(), name='phd_student_list_view'),
    path('staff/', views.StaffListView.as_view(), name='staff_list_view'),
    path('faculty', views.FacultyListView.as_view(), name='faculty_list_view'),
]