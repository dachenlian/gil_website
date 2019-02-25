from pathlib import Path
from django.core.files import File
from .models import MasterStudent, DoctorateStudent, Faculty
import json

print(Path(__file__))
STUDENT_PHOTOS = Path(__file__).parent.joinpath("static/people/gil_photos/student_photos")
FACULTY_PHOTOS = Path(__file__).parent.joinpath("static/people/gil_photos/faculty_photos")
CV_PATH = Path(__file__).parent.joinpath("static/people/cv")

with open(Path(__file__).parent.joinpath("static/people/1071_gil_roster.json")) as fp:
    STUDENT_LIST = json.load(fp)

with open(Path(__file__).parent.joinpath("static/people/gil_faculty.json")) as fp:
    FACULTY_LIST = json.load(fp)


def save_students_to_db(students_lst=STUDENT_LIST):
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


def save_faculty_to_db(faculty_lst=FACULTY_LIST):
    for f in faculty_lst:
        query = Faculty.objects.filter(zh_name=f['zh_name'])
        if query:
            continue
        else:
            profile_picture = FACULTY_PHOTOS / Path(f['eng_name'].lower().replace('-', '_').replace(' ', '_'))
            cv = CV_PATH / Path(f['eng_name'].lower().replace('-', '_').replace(' ', '_') + '_cv.pdf')
            print(profile_picture)
            instance = Faculty(**f)
            try:
                instance.profile_picture.save(profile_picture.name, File(profile_picture.with_suffix('.jpg').open('rb')))
            except FileNotFoundError:
                instance.profile_picture.save(profile_picture.name, File(profile_picture.with_suffix('.png').open('rb')))
            try:
                instance.cv_upload.save(cv.name, File(cv.open('rb')))
            except FileNotFoundError:
                print(f'{instance.eng_name}: CV not found.')
            instance.save()
