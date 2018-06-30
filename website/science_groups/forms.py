from django.forms import ModelForm
from .models import Student, Teacher, Science_Group


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'student_id': 'Номер ИСУ',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество'
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'teacher_id': 'Номер ИСУ',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество'
        }


class ScienceGroupForm(ModelForm):
    class Meta:
        model = Science_Group
        fields = '__all__'
        labels = {
            'group_id': 'Номер группы',
            'teacher': 'Руководитель',
            'students': 'Студенты',
            'group_purpose': 'Назначение'
        }