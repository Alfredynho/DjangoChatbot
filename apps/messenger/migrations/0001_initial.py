# Generated by Django 2.2 on 2019-04-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MessengerUser',
            fields=[
                ('user_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=250, verbose_name='Apellido')),
                ('gender', models.CharField(max_length=250, verbose_name='Genero')),
                ('timezone', models.CharField(max_length=255, verbose_name='Zona Horaria')),
                ('image', models.CharField(max_length=255, verbose_name='image')),
                ('date', models.CharField(max_length=255, verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'ordering': ['user_id'],
            },
        ),
    ]
