from django.http import HttpResponse
import magic
from gil_configuration import settings

mime = magic.Magic(mime=True)


def download(request, file):
    file = settings.MEDIA_ROOT + "/" + file
    with open(file, 'rb') as fp:
        m = mime.from_file(file)
        response = HttpResponse(fp.read(), content_type=m)
        response['content_type'] = m
        response['Content-Disposition'] = f'attachment;filename={file.split("/")[-1]}'
    return response
