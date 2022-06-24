# Generated by Django 2.2 on 2021-09-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1500, verbose_name='Название')),
                ('description', models.CharField(default='', max_length=1500, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(null=True, on_delete=models.CASCADE, to='budemapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Тренинг',
                'verbose_name_plural': 'Тренинги',
                'ordering': ['created_date', 'title'],
            },
        ),
    ]