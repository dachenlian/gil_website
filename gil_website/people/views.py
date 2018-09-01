from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import MasterStudent, DoctorateStudent, Faculty, Staff


class MasterStudentListView(ListView):
    model = MasterStudent

    # context_object_name = 'students'

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = DoctorateStudent.objects.filter(year_of_study='CURRENT')
        context['graduated'] = DoctorateStudent.objects.filter(year_of_study='GRAD')
        return context


class FacultyListView(TemplateView):
    model = Faculty
    # context_object_name = 'faculty_members'
    template_name = 'people/faculty.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = Faculty.objects.filter(status='CURRENT')
        context['retired'] = Faculty.objects.filter(status='RETIRED')
        return context


class StaffListView(TemplateView):
    model = Staff
    context_object_name = 'staff_members'
    template_name = 'people/staff.html'
