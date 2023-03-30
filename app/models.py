from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Категория')
    """"Категории товаров """

def __str__(self)-> str:
    return f'{self.title}'    

class Nike(models.Model):
    """"""
    title = models.CharField(max_length = 255,verbose_name = 'Название Товара')
    description = models.TextField(verbose_name = 'опесание')
    image = models.ImageField(upload_to = 'produkt')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(to = Category,on_delete = models.CASCADE, verbose_name = 'Категории')
    
    def __str__(self) -> str:
        return f'{self.title}'

class Images(models.Model):
    sneakers = models.ForeignKey(to=Nike, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='sneakers_image',verbose_name='Изаброжение')


