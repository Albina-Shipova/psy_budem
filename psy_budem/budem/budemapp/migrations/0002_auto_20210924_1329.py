# Generated by Django 2.2 on 2021-09-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budemapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='short_description',
            field=models.CharField(default='', max_length=700, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='description',
            field=models.CharField(default='', max_length=3000, verbose_name='Описание'),
        ),
    ]