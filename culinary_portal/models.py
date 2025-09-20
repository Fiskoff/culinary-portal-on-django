from django.db import models

# Create your models here.

class Category(models.Model):
    """категории новостей"""
    title = models.CharField(max_length=255, verbose_name="Название категории")  # verbose_name - название поля в админке

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Категория"  # название таблицы в админке
        verbose_name_plural = "Категории"  # название таблицы в админке во множественном числе


class Post(models.Model):
    """Для новостных """
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    content = models.TextField(default="Скоро тут будет статья...", verbose_name="Текст статьи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # Используется при создании, установленное значение не изменяется
    update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления") # Используется при обновлении, автоматически изменяет поле каждый раза, когда объект сохраняется
    photo = models.ImageField(upload_to="photos/", blank=True, null=True, verbose_name="Фото") # Директория в которую буду скачиваться фото. blank=True - не обязательное поля для заполнения, null=True - поле может быть null
    watched = models.IntegerField(default=0, verbose_name="Количество просмотров")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано ли")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория") # Связь с моделью Category

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"