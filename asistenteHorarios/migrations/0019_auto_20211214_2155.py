# Generated by Django 3.2.3 on 2021-12-15 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistenteHorarios', '0018_auto_20211214_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenrap',
            name='Ficha',
        ),
        migrations.AddField(
            model_name='ordenrap',
            name='Ficha',
            field=models.ManyToManyField(to='asistenteHorarios.FichasCaracterizacion'),
        ),
    ]
