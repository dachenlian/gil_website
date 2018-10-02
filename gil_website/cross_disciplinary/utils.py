import csv
from .models import Course


def save_courses_to_db(file, level):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader, None)
        for row in reader:
            print(row)
            name = row[0]
            credit = row[1]
            required = row[2]
            department = row[3]
            professor = row[4]
            note = row[5]

            Course(
                level=level,
                name=name,
                credit=credit,
                required=required,
                department=department,
                professor=professor,
                note=note
            ).save()
