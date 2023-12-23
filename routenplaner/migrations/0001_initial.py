# Generated by Django 3.0.4 on 2020-08-03 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routen',
            },
        ),
        migrations.CreateModel(
            name='Ort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField(default=0, verbose_name='Position')),
                ('aktiv', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('adresse', models.CharField(max_length=100, verbose_name='Adresse')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orte', to='routenplaner.Route')),
            ],
            options={
                'verbose_name': 'Ort',
                'verbose_name_plural': 'Orte',
            },
        ),
    ]
