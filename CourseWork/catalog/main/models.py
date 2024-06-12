from django.db import models


class Product(models.Model):
    name = models.CharField('Наименование', max_length=200)
    price = models.IntegerField('Цена')
    width = models.IntegerField('Ширина')
    thickness = models.FloatField('Толщина')
    safe_layer = models.FloatField('Толщина защитного слоя')
    fire_safety = models.CharField('Класс пожарной безопасности', max_length=5, blank=True)
    brand = models.CharField('Бренд', max_length=20, blank=True)
    link = models.CharField('Ссылка', max_length=200)
    photo = models.CharField('Фото', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
