from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_do = models.DateTimeField(verbose_name="Время завершения")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнена")
    color_id = models.ForeignKey('Color', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"


class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name="Стиль")
    ru_name = models.CharField(max_length=255, verbose_name="Цвет")

    def __str__(self):
        return self.ru_name or "Неизвестный"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
