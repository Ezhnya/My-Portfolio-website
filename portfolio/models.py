from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    link = models.URLField(blank=True, null=True, verbose_name="Посилання")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
