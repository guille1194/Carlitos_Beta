# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_curso', models.IntegerField(unique=True)),
                ('curso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_paciente', models.CharField(max_length=99)),
                ('apellido_paciente', models.CharField(max_length=99)),
                ('num_expediente', models.IntegerField()),
                ('area', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('fecha_conclusion', models.DateField(default=django.utils.timezone.now)),
                ('evaluacion_completa', models.CharField(max_length=2)),
                ('reportes', models.CharField(max_length=2)),
                ('diagnostico', models.CharField(max_length=45)),
                ('fecha_nacimiento', models.DateField(default=django.utils.timezone.now)),
                ('edad_ingreso', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('perfil_usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profesionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profesionista', models.CharField(max_length=68)),
                ('apellido_profesionista', models.CharField(max_length=68)),
                ('reportes', models.CharField(max_length=2)),
                ('horario', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carlos_Home.Cursos')),
                ('perfil_usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
