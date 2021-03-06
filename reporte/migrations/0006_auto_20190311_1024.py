# Generated by Django 2.1.5 on 2019-03-11 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0005_auto_20190307_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diario',
            options={'ordering': ['-pk'], 'verbose_name': 'Reporte diario', 'verbose_name_plural': 'Reportes Diarios'},
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_1', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_2', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_3', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_4', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_5', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_6', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_7', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_8', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='act_9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actividad_9', to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reporte.Actividad', verbose_name='Actividad a realizar'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='proyecto.Proyectos', verbose_name='Proyecto'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsable', to=settings.AUTH_USER_MODEL, verbose_name='Responsable en sitio'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supervisor', to=settings.AUTH_USER_MODEL, verbose_name='Supervisor de seguridad y ambiente'),
        ),
    ]
