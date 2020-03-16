<<<<<<< HEAD
# Generated by Django 3.0.3 on 2020-03-06 22:50
=======
# Generated by Django 3.0.3 on 2020-03-14 15:28
>>>>>>> develop

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('autenticacion', '0001_initial'),
=======
        ('autenticacion', '__first__'),
>>>>>>> develop
    ]

    operations = [
        migrations.CreateModel(
            name='Control_medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('peso', models.FloatField()),
                ('talla', models.FloatField()),
                ('pd', models.FloatField()),
                ('alimentacion', models.CharField(max_length=200)),
                ('hierro', models.FloatField()),
                ('vit_D', models.FloatField()),
                ('observaciones', models.TextField()),
                ('presion_arterial', models.FloatField()),
                ('proximo_control', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
<<<<<<< HEAD
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='autenticacion.Usuario')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> develop
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_de_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('documento_de_Identidad', models.CharField(max_length=200)),
                ('lugar_de_nacimiento', models.CharField(max_length=200)),
                ('tipo_persona', models.CharField(choices=[('a', 'Tutor'), ('b', 'Doctor'), ('c', 'Nino')], max_length=1)),
            ],
<<<<<<< HEAD
            bases=('autenticacion.usuario',),
=======
>>>>>>> develop
        ),
        migrations.CreateModel(
            name='Tipo_de_tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_tutor', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carnets.Persona')),
                ('tipo_especializacion', models.CharField(choices=[('Aler.', 'Alergología'), ('Anes.', 'Anestesiología'), ('Card.', 'Cardiología'), ('Gast.', 'Gastroenterología'), ('Endo.', 'Endocrinología'), ('Geri.', 'Geriatría'), ('Hema.', 'Hematología'), ('Infe.', 'Infectología'), ('Aeroes', 'Medicina aeroespacial'), ('Depo', 'Medicina del deporte'), ('Traba', 'Medicina del trabajo'), ('Urgenc', 'Medicina de urgencias'), ('Famili', 'Medicina familiar y comunitaria'), ('Física', 'Medicina física y rehabilitación'), ('Intens', 'Medicina intensiva'), ('Intern', 'Medicina interna'), ('Forens', 'Medicina forense'), ('Preventiva.', 'Medicina preventiva y salud pública'), ('Nefr.', 'Nefrología'), ('Neum.', 'Neumología'), ('Neur.', 'Neurología'), ('Nutr.', 'Nutriología'), ('Onco.', 'Oncología médica'), ('Onco.', 'Oncología radioterápica'), ('Pedi.', 'Pediatría'), ('Psiq.', 'Psiquiatría'), ('Reum.', 'Reumatología'), ('Toxi.', 'Toxicología')], max_length=11)),
<<<<<<< HEAD
=======
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.Usuario')),
>>>>>>> develop
            ],
            bases=('carnets.persona',),
        ),
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carnets.Persona')),
                ('servicio_de_salud', models.CharField(max_length=200)),
            ],
            bases=('carnets.persona',),
        ),
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Control_medico')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_control', models.DateField()),
                ('control_medico', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Control_medico')),
                ('medico_asignado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carnets.Persona')),
                ('agenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Agenda')),
<<<<<<< HEAD
                ('hijos', models.ManyToManyField(through='carnets.Tipo_de_tutor', to='carnets.Nino')),
=======
                ('hijos', models.ManyToManyField(blank=True, null=True, through='carnets.Tipo_de_tutor', to='carnets.Nino')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.Usuario')),
>>>>>>> develop
            ],
            bases=('carnets.persona',),
        ),
        migrations.AddField(
            model_name='tipo_de_tutor',
            name='nino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Nino'),
        ),
        migrations.AddField(
            model_name='tipo_de_tutor',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Tutor'),
        ),
        migrations.AddField(
            model_name='nino',
            name='carnet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carnets.Carnet'),
        ),
        migrations.AddField(
            model_name='nino',
            name='medico_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Medico'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='nino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carnets.Nino'),
        ),
    ]
