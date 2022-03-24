from django.db import models
from django.urls import reverse


class Blog(models.Model):
    name = models.CharField(max_length=255, default="Это мой блог", verbose_name="Название")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(max_length=500, blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        ordering = ['id']
