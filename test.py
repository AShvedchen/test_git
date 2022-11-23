student_list = []


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_rating(self):
        if not self.grades:
            return 0
        grades_list = []
        for data in self.grades.values():
            grades_list.extend(data)
        return round(sum(grades_list) / len(grades_list), 1)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Cравнение некорректно'
        return self.average_rating() < other.average_rating()

    def __str__(self):
        string__courses_in_progress = ', '.join(self.courses_in_progress)
        string__finished_courses = ', '.join(self.finished_courses)
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {Student.average_rating(self)} \nКурсы в процессе изучения: {string__courses_in_progress}\nЗавершенные курсы: {string__finished_courses}'


lecturer_list = []


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_list.append(self)

    def average_rating(self):
        if not self.grades:
            return 0
        grades_list = []
        for data in self.grades.values():
            grades_list.extend(data)
        return round(sum(grades_list) / len(grades_list), 1)

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {Lecturer.average_rating(self)}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\n'


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Python']
student1.grades['Git'] = [9, 10, 5, 10, 10]
student1.grades['Python'] = [10, 10]

student2 = Student('Eman2', 'Ruoy2', 'your_gender')
student2.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Git']
student2.grades['Python'] = [7, 10, 5, 1, 10]
student2.grades['Git'] = [10, 10, 1]

reviewer1 = Reviewer('Buddy', 'Some')
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 3)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 10)

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 1)
student1.rate_lecturer(lecturer1, 'Python', 10)

student2.rate_lecturer(lecturer1, 'Git', 10)
student2.rate_lecturer(lecturer1, 'Git', 9)
student2.rate_lecturer(lecturer1, 'Git', 10)

print(f'Студент--> {student1}\n')
print(f'Студент--> {student2}\n')
print(f'Лектор--> {lecturer1}\n')
print(f'Проверяющий--> {reviewer1}\n')
print(student1 > student2)



def average_grade_students(student_list, name_course):
    grades_list = []
    for student in student_list:
        grades_list.extend(student.grades.get(name_course, []))
    if not grades_list:
        return "Такой курс сейчас никто не проходит"
    return round(sum(grades_list) / len(grades_list), 1)


def average_grade_lecturer(lecturer_list, name_course):
    grades_list = []
    for lecturer in lecturer_list:
        grades_list.extend(lecturer.grades.get(name_course, []))
    if not grades_list:
        return "Такой курс сейчас никто не проходит"
    return round(sum(grades_list) / len(grades_list), 1)


while True:

    name_course = input('Введите курс для вывода средней оценки результатов:\n')

    if name_course == 'Git':
        print(
            f'Средняя оценка для всех студентов по курсу {name_course}: {average_grade_students(student_list, name_course)}\nСредняя оценка для всех лекторов по курсу {name_course}: {average_grade_lecturer(lecturer_list, name_course)}'
        )

    elif name_course == 'Python':
        print(
            f'Средняя оценка для всех студентов по курсу {name_course}: {average_grade_students(student_list, name_course)}\nСредняя оценка для всех лекторов по курсу {name_course}: {average_grade_lecturer(lecturer_list, name_course)}'
        )