# Generated by Django 3.0.3 on 2020-03-15 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carnets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nino',
            name='foto_perfil',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]