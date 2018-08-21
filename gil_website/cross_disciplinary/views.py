from django.views.generic import TemplateView


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
