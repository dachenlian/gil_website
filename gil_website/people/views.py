from django.views.generic.list import ListView
from .models import MasterStudent, DoctorateStudent, Faculty, Staff


class MasterStudentListView(ListView):
    model = MasterStudent

    context_object_name = 'students'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = MasterStudent.objects.filter(year_of_study='FIRST')
        context['second'] = MasterStudent.objects.filter(year_of_study='SECOND')
        context['third'] = MasterStudent.objects.filter(year_of_study='THIRD')
        context['fourth'] = MasterStudent.objects.filter(year_of_study='FOURTH')
        context['graduated'] = MasterStudent.objects.filter(year_of_study='GRAD')
        return context
    template_name = 'people/ma_students.html'


class DoctorateStudentListView(ListView):
    model = DoctorateStudent
    context_object_name = 'students'
    template_name = 'people/phd_students.html'


class FacultyListView(ListView):
    model = Faculty
    context_object_name = 'faculty_members'
    template_name = 'people/faculty.html'


class StaffListView(ListView):
    model = Staff
    context_object_name = 'staff_members'
    template_name = 'people/staff.html'
