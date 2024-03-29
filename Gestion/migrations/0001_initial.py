# Generated by Django 2.2.1 on 2019-07-19 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asignaturas',
            fields=[
                ('asig_codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('asig_codigo_port', models.CharField(max_length=20)),
                ('asig_nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='carreras',
            fields=[
                ('car_codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('carr_nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='facultades',
            fields=[
                ('fac_codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fac_nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='paralelos',
            fields=[
                ('par_codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('par_nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='periodo',
            fields=[
                ('per_cod', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('per_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('usr_cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('usr_clave', models.CharField(max_length=20)),
                ('usr_tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='semestre',
            fields=[
                ('sem_codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sem_nombre', models.CharField(max_length=100)),
                ('car_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.carreras')),
                ('par_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.paralelos')),
                ('per_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_nombres', models.CharField(max_length=50)),
                ('per_apellidos', models.CharField(max_length=50)),
                ('per_correo', models.CharField(max_length=100)),
                ('usr_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='det_persona_asignaturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asig_codigo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestion.asignaturas')),
                ('usr_cedula', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestion.persona')),
            ],
        ),
        migrations.AddField(
            model_name='carreras',
            name='far_codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.facultades'),
        ),
        migrations.AddField(
            model_name='asignaturas',
            name='sem_codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.semestre'),
        ),
    ]
