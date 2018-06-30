from django.urls import path
from . import views

urlpatterns = [

    ### добавление, изменение, удаление студентов
    # /student/add
    path('student/add/', views.add_student, name='student-add'),
    # /student/<student_id>/edit
    path('student/<int:student_id>/edit/', views.edit_student, name='student-edit'),
    # /student/<student_id/delete
    path('student/<int:student_id>/delete/', views.delete_student, name='student-delete'),


    ### добавление, изменение, удаление преподавателей
    # /teacher/add
    path('teacher/add/', views.teacher_add, name='teacher-add'),
    # /teacher/<teacher_id>/edit
    path('teacher/<int:teacher_id>/edit/', views.teacher_edit, name='teacher-edit'),
    # /teacher/<teacher_id>/delete
    path('teacher/<int:teacher_id>/delete/', views.teacher_delete, name='teacher-delete'),


    ### добавление, изменение, удаление научных групп
    # /group/create
    path('group/create', views.create_group, name='group-create'),
    # /groups/<group_id/delete
    path('groups/<int:group_id>/delete/', views.delete_group, name='group-delete'),
    # /groups/<group_id>/edit
    path('groups/<int:group_id>/edit/', views.edit_group, name='group-edit'),

    ### информация о конкретном студенте/преподавателе/научной группе
    # /groups/<group_id>
    path('group/<int:group_id>/', views.group_details, name='group_details'),
    # /teacher/<teacher_id>
    path('teacher/<int:teacher_id>/', views.teacher_details, name='teacher_details'),
    # /student/<student_id>
    path('student/<int:student_id>/', views.student_details, name='student_details'),


    ### список студентов, преподавателей, научных групп
    # /groups/
    path('groups/', views.science_groups, name='groups'),
    # /teachers/
    path('teachers/', views.teachers, name='teachers'),
    # /students/
    path('students/', views.students, name='students'),
    # /
    path('', views.index, name='index'),
]