# Generated by Django 2.1.5 on 2019-02-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_auto_20190213_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='estudios',
            field=models.ManyToManyField(related_name='get_posts', to='proyecto.Estudios', verbose_name='Estudios'),
        ),
    ]