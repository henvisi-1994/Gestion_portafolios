# Generated by Django 2.2.1 on 2019-07-30 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0005_usuarios_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignaturas',
            name='asig_clave',
            field=models.CharField(default='', max_length=100),
        ),
    ]
