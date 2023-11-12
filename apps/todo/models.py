from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    is_complated = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    image = models.ImageField(
        upload_to="todo_image/",
        verbose_name="Фото"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"