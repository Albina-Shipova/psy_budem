# Generated by Django 2.2 on 2021-09-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budemapp', '0005_seminar_on_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='date_of_seminar',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Дата и время'),
        ),
    ]
