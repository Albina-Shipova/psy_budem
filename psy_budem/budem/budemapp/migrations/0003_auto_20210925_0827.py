# Generated by Django 2.2 on 2021-09-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budemapp', '0002_auto_20210924_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='date_of_seminar',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='short_description',
            field=models.CharField(default='', max_length=700, verbose_name=' Краткое описание'),
        ),
    ]
