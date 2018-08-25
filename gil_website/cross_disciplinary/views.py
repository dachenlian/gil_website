from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.views.generic.base import View
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = "cross_disciplinary/index.html"


class PurposeView(TemplateView):
    template_name = "cross_disciplinary/purpose.html"


class RequirementsView(TemplateView):
    template_name = "cross_disciplinary/requirements.html"


class CourseInfoView(TemplateView):
    template_name = "cross_disciplinary/course_info.html"


class StudentAreaView(TemplateView):
    template_name = "cross_disciplinary/student_area.html"


class SignUpView(FormView):
    template_name = "cross_disciplinary/signup.html"
    form_class = SignUpForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        user.profile.student_id = form.cleaned_data.get('student_id')
        user.profile.eng_name = form.cleaned_data.get('eng_name')
        user.profile.zh_name = form.cleaned_data.get('zh_name')
        user.profile.gender = form.cleaned_data.get('gender')
        user.profile.college = form.cleaned_data.get('college')
        user.profile.department = form.cleaned_data.get('department')
        user.profile.reason = form.cleaned_data.get('reason')
        user.profile.primary_email = form.cleaned_data.get('primary_email')
        user.profile.address = form.cleaned_data.get('address')
        user.profile.profile_picture = form.cleaned_data.get('profile_picture')
        user.profile.more_info = form.cleaned_data.get('more_info')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, "User successfully added!")
        return super().form_valid(form)



