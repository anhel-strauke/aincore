# Generated by Django 2.0.5 on 2019-01-14 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_course_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetablealteration',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
