import requests
from bs4 import BeautifulSoup as bs


def get_zhenshi(url, year):
    r = requests.get(url)
    r.encoding = 'big5'
    soup = bs(r.text)
    base_path = "http://gra103.aca.ntu.edu.tw/brochure/{}{}"
    rel_path = soup.find_all('a', string='1120語言學研究所碩士班')[0]['href'][1:]
    abs_path = base_path.format(year, rel_path)

    return abs_path


def remove_attrs(bs_lst):
    for tag in bs_lst:
        try:
            del tag.attrs
        except AttributeError:
            pass
        for inner in tag.contents:
            try:
                del inner.attrs
            except AttributeError:
                pass

    return bs_lst


def change_tag(element, new_tag):
    for tag in element.contents:
        try:
            tag.name = new_tag
        except AttributeError:
            pass

    return element


def get_requirements_table(url):
    r = requests.get(url).text
    soup = bs(r, 'html5lib')

    requirements_table = soup.select("table:nth-of-type(1) tbody tr")
    remove_attrs(requirements_table)
    change_tag(requirements_table[0], 'th')

    other_requirements = soup.select("table:nth-of-type(2) tbody tr")
    remove_attrs(other_requirements)

    special_header = other_requirements[0].select("td:nth-of-type(1)")[0].text
    special_body = other_requirements[0].select("td:nth-of-type(2)")[0].text
    remarks_header = other_requirements[1].select("td:nth-of-type(1)")[0].text
    remarks_body = other_requirements[1].select("td:nth-of-type(2)")[0].text

    requirements_header = "".join(str(r) for r in requirements_table[0])
    requirements_body = "".join(str(r) for r in requirements_table[1:])

    return {
        'requirements_header': requirements_header,
        'requirements_body': requirements_body,
        'special_header': special_header,
        'special_body': special_body,
        'remarks_header': remarks_header,
        'remarks_body': remarks_body,
    }

