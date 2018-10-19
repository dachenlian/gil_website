from pathlib import Path
from django.core.files import File
from .models import MasterStudent, DoctorateStudent
import json

print(Path(__file__))
STUDENT_PHOTOS = Path(__file__).parent.joinpath("static/people/gil_photos/student_photos")

with open(Path(__file__).parent.joinpath("static/people/1071_gil_roster.json")) as fp:
    STUDENT_LIST = json.load(fp)


def save_students_to_db(students_lst):
    for student in students_lst:
        student = dict(student)
        if student['degree'] == 'ma':
            model = MasterStudent
        else:
            model = DoctorateStudent
        query = model.objects.filter(zh_name=student['zh_name'])
        if query:
            continue
        else:
            profile_picture = STUDENT_PHOTOS / Path(student['eng_name'].lower().replace('-', '_').replace(' ', '_'))
            print(profile_picture)
            del student['degree']
            instance = model(**student)
            try:
                instance.profile_picture.save(profile_picture.name, File(profile_picture.with_suffix('.jpg').open('rb')))
            except FileNotFoundError:
                instance.profile_picture.save(profile_picture.name, File(profile_picture.with_suffix('.png').open('rb')))
            instance.save()


def save_faculty_to_db(model, faculty):
    for f in faculty:
        query = model.objects.filter(zh_name=f['zh_name'])
        if query:
            continue
        else:
            model(**f).save()
