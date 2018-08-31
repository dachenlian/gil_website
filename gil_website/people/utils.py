def save_students_to_db(model, students_lst):
    for students in students_lst:
        for student in students:
                query = model.objects.filter(zh_name=student['zh_name'])
                if query:
                    continue
                else:
                    model(**student).save()


def save_faculty_to_db(model, faculty):
    for f in faculty:
        query = model.objects.filter(zh_name=f['zh_name'])
        if query:
            continue
        else:
            model(**f).save()
