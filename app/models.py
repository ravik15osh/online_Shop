from django.db import models
from user.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Категория')
    """"Категории товаров """

    def __str__(self)-> str:
        return f'{self.title}'    

class Nike(models.Model):
    """Товары"""
    title = models.CharField(max_length = 255,verbose_name = 'Название Товара')
    description = models.TextField(verbose_name = 'опесание')
    image = models.ImageField(upload_to = 'produkt')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(to = Category,on_delete = models.CASCADE, verbose_name = 'Категории')
    
    def __str__(self) -> str:
        return f'{self.title}'

class Images(models.Model):
    sneakers = models.ForeignKey(to=Nike, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='sneakers_image',verbose_name='Фото')
    """Фото"""


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name = 'Оформление Заказы на товаров')
    total_price = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    messege = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(unique=True,null=True,blank=True)
    """Оформление Заказы на товаров"""
    
    def __str__(self) -> str:
        return f'{self.address}'
    
class OrderItem(models.Model):
    product = models.ForeignKey(to=Nike, on_delete=models.CASCADE, verbose_name = 'Время Заказа')
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    """Время Заказа"""
    
    def __str__(self) -> str:
        return f'{self.product} {self.order}'