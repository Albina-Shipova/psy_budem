from django.db import models
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField


class Seminar(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Название')
    description = RichTextField(max_length=3000, default='', verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_of_seminar = models.CharField(max_length=100, verbose_name='Дата и время', blank=True, default='',
                                       editable=True)
    on_main_page = models.BooleanField(default=False, verbose_name='Ближайшие семинары')
    more_info = RichTextField(max_length=3000, verbose_name='Дополнительная информация', blank=True, default='')

    def get_absolute_url(self):
        return reverse_lazy('seminar', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренинг'
        verbose_name_plural = 'Тренинги'
        ordering = ['created_date', 'title']


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    text = RichTextField(max_length=2000, verbose_name='Отзыв')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

