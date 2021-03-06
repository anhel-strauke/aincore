# Generated by Django 2.0.5 on 2019-01-14 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import python_course_2.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.SlugField()),
                ('visible', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.SlugField(max_length=30, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('hours', models.FloatField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='python_course_2.Course')),
            ],
        ),
        migrations.CreateModel(
            name='LessonLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='python_course_2.Lesson')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='LinkPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReadingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=python_course_2.models.reading_item_index_default)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='TimetableAlteration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(0, 0))),
                ('end_time', models.TimeField(default=datetime.time(0, 0))),
                ('cancelled', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_alterations', to='python_course_2.Course')),
            ],
        ),
        migrations.CreateModel(
            name='TimetableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='python_course_2.Course')),
            ],
            options={
                'ordering': ['weekday'],
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='python_course_2.Course'),
        ),
    ]
