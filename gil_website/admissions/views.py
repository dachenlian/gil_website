from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup as bs
import datetime

from .utils import get_requirements_table, get_zhenshi


CURRENT_YEAR = datetime.datetime.now().year
ACADEMIC_YEAR = CURRENT_YEAR - 1911


class IndexView(TemplateView):
    template_name = "admissions/index.html"


class MAZhenshiView(TemplateView):
    template_name = "admissions/zhenshi.html"
    url = "http://gra103.aca.ntu.edu.tw/brochure/{}/detail.asp"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regulations'] = get_zhenshi(self.url.format(ACADEMIC_YEAR), ACADEMIC_YEAR)
        context['year'] = ACADEMIC_YEAR
        return context


class MARegularView(TemplateView):
    template_name = "admissions/ma_regular.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regulations'] = f"http://gra103.aca.ntu.edu.tw/gra_regular/" \
                                 f"{ACADEMIC_YEAR}%E7%B0%A1%E7%AB%A0/pdf/112.pdf"
        context['year'] = ACADEMIC_YEAR
        return context


class MADegreeRequirements(TemplateView):
    template_name = "admissions/ma_degree_requirements.html"
    url = "http://gra108.aca.ntu.edu.tw/graVoxCourse/index.php/gquery/MainPage?INYEAR={}&DPGCODE=R1-14201"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requirements_table'] = get_requirements_table(self.url.format(ACADEMIC_YEAR))
        return context


class PhDDegreeRequirements(TemplateView):
    template_name = "admissions/phd_degree_requirements.html"
    url = "http://gra108.aca.ntu.edu.tw/graVoxCourse/index.php/gquery/MainPage?INYEAR={}&DPGCODE=D-14202"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requirements_table'] = get_requirements_table(self.url.format(ACADEMIC_YEAR))
        return context
