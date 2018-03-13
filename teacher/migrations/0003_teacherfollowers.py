# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-10 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teachertypesship'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherFollowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follower_id', models.CharField(help_text='收藏者id', max_length=64, verbose_name='收藏者id')),
                ('follower_type', models.IntegerField(default=2, help_text='1：老师 2：学生', verbose_name='收藏者类型, 目前教师仅能被学生收藏')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('teacher', models.ForeignKey(help_text='教师', on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
            options={
                'verbose_name': '被收藏老师',
                'verbose_name_plural': '被收藏老师',
            },
        ),
    ]