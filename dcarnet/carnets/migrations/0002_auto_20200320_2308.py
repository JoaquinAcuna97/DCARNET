# Generated by Django 3.0.3 on 2020-03-21 02:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carnets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carnet',
            name='control_medico',
        ),
        migrations.AddField(
            model_name='carnet',
            name='fecha_de_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='control_medico',
            name='carnet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Carnet'),
        ),
        migrations.AddField(
            model_name='control_medico',
            name='fecha_de_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
