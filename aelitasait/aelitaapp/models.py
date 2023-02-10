from django.db import models
from django.urls import reverse


class Doctors(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="ФИО")
    title = models.CharField(max_length=200, verbose_name='Должность')
    about = models.TextField(verbose_name="Подробнее", default="Информации нет")
    picture = models.ImageField(upload_to='aelitaapp/photos/%Y/%m/%d', verbose_name='Фото')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'doctors'
        verbose_name = "Доктора"
        verbose_name_plural = "Доктора"
        ordering = ['name']


class Price (models.Model):
    name = models.CharField(max_length=300, db_index=True, verbose_name="Название")
    price = models.IntegerField(default=0, verbose_name="Цена")
    id_cat = models.ForeignKey('Categorys', null=False, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'price'
        verbose_name = "Цены"
        verbose_name_plural = "Цены"
        ordering = ['name']

class Categorys (models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('price', kwargs={'price_slug': self.slug})

    class Meta:
        db_table = 'categorys'
        verbose_name = "Категории"
        verbose_name_plural = "Категории"