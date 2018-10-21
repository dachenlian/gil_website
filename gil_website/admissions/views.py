from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup as bs
import datetime

from .utils import get_requirements_table


CURRENT_YEAR = datetime.datetime.now().year
ACADEMIC_YEAR = CURRENT_YEAR - 1911


class IndexView(TemplateView):
    template_name = "admissions/index.html"


class ZhenshiView(TemplateView):
    template_name = "admissions/zhenshi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regulations'] = f"http://gra103.aca.ntu.edu.tw/gra_regular/" \
                                 f"{ACADEMIC_YEAR}%E7%B0%A1%E7%AB%A0/pdf/112.pdf"
        context['hi'] = "HI"
        return context


class MADegreeRequirements(TemplateView):
    template_name = "admissions/ma_degree_requirements.html"
    url = "http://gra108.aca.ntu.edu.tw/graVoxCourse/index.php/gquery/MainPage?INYEAR={}&DPGCODE=R1-14201"
    html = requests.get(url.format(ACADEMIC_YEAR)).text
    print(html)
    soup = bs(html, 'html5lib')
    required_courses = "".join(str(tag) for tag in soup.select("table:nth-of-type(1) *"))
    print(required_courses)
    other_requirements = soup.select("table.tab1:nth-of_type(2)")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requirements_table'] = get_requirements_table(self.url.format(ACADEMIC_YEAR))
        print(context['requirements_table'])
        return context


