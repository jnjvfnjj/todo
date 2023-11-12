from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(
        max_length=255,
        verbose_name='email'
    )
    phone_number = models.CharField(
        verbose_name="Телефонный номер", 
        max_length=20
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    age = models.IntegerField(
        verbose_name="Возраст",
        null=True,
        blank=True
    )
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"