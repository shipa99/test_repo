# Generated by Django 3.0.6 on 2020-06-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0007_auto_20200607_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(default='2000-01-01', verbose_name='Дата рождения'),
        ),
    ]
