# Generated by Django 2.1a1 on 2018-06-05 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('science_groups', '0008_auto_20180605_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='science_group',
            name='students',
        ),
        migrations.RemoveField(
            model_name='science_group',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Science_Group',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
