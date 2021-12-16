# Generated by Django 3.2.3 on 2021-12-15 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistenteHorarios', '0015_auto_20211123_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ficha', models.ManyToManyField(to='asistenteHorarios.FichasCaracterizacion')),
                ('ordenRap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistenteHorarios.ordenrap')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistenteHorarios.resultados')),
            ],
        ),
        migrations.AlterField(
            model_name='ordenrap',
            name='Resultado',
            field=models.ManyToManyField(through='asistenteHorarios.auxiliar', to='asistenteHorarios.Resultados'),
        ),
    ]
