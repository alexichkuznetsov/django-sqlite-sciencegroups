# Generated by Django 2.1a1 on 2018-06-05 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('science_groups', '0012_auto_20180605_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Science_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('group_purpose', models.CharField(max_length=300)),
                ('students', models.ManyToManyField(to='science_groups.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='science_group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='science_groups.Teacher'),
        ),
    ]