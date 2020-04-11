# Generated by Django 3.0.4 on 2020-04-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0004_personalfit_personalfituioption'),
        ('mall', '0002_auto_20200411_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='personal_fits',
            field=models.ManyToManyField(help_text='입력 받아야 할 특징 치수의 개인화 데이터들의 모음입니다.', through='fit.PersonalFitUIOption', to='fit.PersonalFit', verbose_name='특징 치수 개인화 데이터 모음'),
        ),
    ]
