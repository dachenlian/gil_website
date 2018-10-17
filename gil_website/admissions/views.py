from django.views.generic import TemplateView
import requests
import datetime


class IndexView(TemplateView):
    template_name = "admissions/index.html"


class ZhenshiView(TemplateView):
    template_name = "admissions/zhenshi.html"
    current_year = datetime.datetime.now().year
    academic_year = current_year - 1911

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regulations'] = f"http://gra103.aca.ntu.edu.tw/gra_regular/" \
                                 f"{self.academic_year}%E7%B0%A1%E7%AB%A0/pdf/112.pdf"
        context['hi'] = "HI"
        return context
