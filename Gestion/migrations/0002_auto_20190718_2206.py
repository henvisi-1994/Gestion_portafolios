# Generated by Django 2.2.1 on 2019-07-19 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='det_persona_asignaturas',
            name='asig_codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.asignaturas'),
        ),
    ]
