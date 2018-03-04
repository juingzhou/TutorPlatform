# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-04 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import libs.uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('common', '0004_auto_20180301_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uid', models.CharField(default=libs.uuid.create_teacher_uid, max_length=16, unique=True, verbose_name='教师ID')),
                ('last_name', models.CharField(max_length=4, verbose_name='姓氏')),
                ('phone', models.CharField(max_length=16, verbose_name='电话')),
                ('sex', models.IntegerField(default=0, help_text='0：女 1：男', verbose_name='性别')),
                ('learn', models.IntegerField(choices=[(0, '暂无'), (1, '本科'), (2, '研究生')], default=0, verbose_name='学历')),
                ('profession', models.CharField(blank=True, max_length=32, null=True, verbose_name='专业')),
                ('high_score', models.IntegerField(default=0, verbose_name='高考分数')),
                ('money', models.IntegerField(default=0, help_text='默认单位：小时', verbose_name='期望薪资')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('head_image', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('self_introduction', models.CharField(blank=True, max_length=1000, null=True, verbose_name='自我介绍')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.City', verbose_name='城市')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='用户')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.School', verbose_name='学校')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherSubjectsShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subject', to='common.Subject', verbose_name='学科')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher', verbose_name='教师')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
