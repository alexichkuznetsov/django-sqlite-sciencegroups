from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import StudentForm, TeacherForm, ScienceGroupForm


def index(request):
    template = loader.get_template('science_groups/index.html')
    return HttpResponse(template.render())

def students(request):
    students = Student.objects.order_by('student_id')
    template = loader.get_template('science_groups/students.html')

    context = {
        'students': students
    }

    return HttpResponse(template.render(context, request))


def student_details(request, student_id):
    student = Student.objects.get(student_id=student_id)
    groups = student.science_group_set.all()
    template = loader.get_template('science_groups/student_details.html')

    context = {
        'student': student,
        'groups': groups
    }

    return HttpResponse(template.render(context, request))


def teachers(request):
    teachers = Teacher.objects.order_by('teacher_id')
    template = loader.get_template('science_groups/teachers.html')

    context = {
        'teachers': teachers
    }

    return HttpResponse(template.render(context, request))


def teacher_details(request, teacher_id):
    teacher = Teacher.objects.get(teacher_id=teacher_id)
    groups = teacher.science_group_set.all()
    template = loader.get_template('science_groups/teacher_details.html')

    context = {
        'teacher': teacher,
        'groups': groups
    }

    return HttpResponse(template.render(context, request))


def science_groups(request):
    groups = Science_Group.objects.all()
    template = loader.get_template('science_groups/groups.html')

    context = {
        'groups': groups
    }

    return HttpResponse(template.render(context, request))


def group_details(request, group_id):
    group = Science_Group.objects.get(group_id=group_id)
    students = group.students.all()
    template = loader.get_template('science_groups/group_details.html')

    context = {
        'group': group,
        'students': students
    }

    return HttpResponse(template.render(context, request))


def add_student(request):
    template = 'science_groups/student_form.html'
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentForm()

    context = {
        'form': form
    }

    return render(request, template, context)


def edit_student(request, student_id):
    template = 'science_groups/student_form.html'
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        try:
            if form.is_valid():
                student_id = form.cleaned_data['student_id']
                form.save()
                return HttpResponseRedirect(reverse('student_details', kwargs={'student_id': student_id}))
        except Exception:
            return HttpResponse('<p>Что-то пошло не так во время редактирования...</p>')

    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student
    }

    return render(request, template, context)


def delete_student(request, student_id):
    template = 'science_groups/student_form.html'
    student = get_object_or_404(Student, student_id=student_id)

    try:
        if request.method == 'POST':
            student.delete()
            return HttpResponseRedirect(reverse('students'))
        else:
            form = StudentForm(instance=student)
    except Exception:
        return HttpResponse('<p>Что-то пошло не так во время удаления...</p>')

    context = {
        'form': form,
        'student': student
    }

    return render(request, template, context)


def teacher_add(request):
    template = 'science_groups/teacher_form.html'

    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherForm()

    context = {
        'form': form
    }

    return render(request, template, context)


def teacher_edit(request, teacher_id):
    template = 'science_groups/teacher_form.html'

    try:
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)

        if request.method == 'POST':
            form = TeacherForm(request.POST, instance=teacher)
            if form.is_valid():
                teacher_id = form.cleaned_data['teacher_id']
                form.save()
                return HttpResponseRedirect(reverse('teacher_details', kwargs={'teacher_id': teacher_id}))
        else:
            form = TeacherForm(instance=teacher)
    except Teacher.DoesNotExist:
        raise Http404('Такого преподавателя не существует')

    context = {
        'form': form,
        'teacher': teacher
    }

    return render(request, template, context)



def teacher_delete(request, teacher_id):
    template = 'science_groups/teacher_form.html'

    try:
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)

        if request.method == 'POST':
            form = TeacherForm(request.POST)
            teacher.delete()
            return HttpResponseRedirect(reverse('teachers'))
        else:
            form = TeacherForm(instance=teacher)
    except Teacher.DoesNotExist:
        raise Http404('Такого преподавателя не существует')

    context = {
        'form': form,
        'teacher': teacher
    }

    return render(request, template, context)


def create_group(request):
    template = 'science_groups/group_form.html'

    if request.method == 'POST':
        form = ScienceGroupForm(request.POST)
        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            form.save()
            return HttpResponseRedirect(reverse('group_details', kwargs={'group_id': group_id}))
    else:
        form = ScienceGroupForm()

    context = {
        'form': form
    }

    return render(request, template, context)


def edit_group(request, group_id):
    template = 'science_groups/group_form.html'
    group = Science_Group.objects.get(group_id=group_id)

    if request.method == 'POST':
        form = ScienceGroupForm(request.POST, instance=group)

        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            form.save()
            return HttpResponseRedirect(reverse('group_details', kwargs={'group_id': group_id}))
    else:
        form = ScienceGroupForm(instance=group)

    context = {
        'form': form,
        'group': group
    }

    return render(request, template, context)


def delete_group(request, group_id):
    template = 'science_groups/group_delete_form.html'

    try:
        group = get_object_or_404(Science_Group, group_id=group_id)
        if request.method == 'POST':
            group.delete()
            return HttpResponseRedirect(reverse('groups'))
        else:
            form = ScienceGroupForm(instance=group)
    except Science_Group.DoesNotExist:
        raise Http404('Такой группы не существует')

    context = {
        'form': form,
        'group': group
    }

    return render(request, template, context)
