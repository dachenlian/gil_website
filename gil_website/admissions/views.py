from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "admissions/index.html"


class ZhenshiView(TemplateView):
    template_name = "admissions/zhenshi.html"