from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Progress(models.Model):
    elevation = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Progress")
        verbose_name_plural = ("Progress")

    def __str__(self):
        return self.elevation


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=False)
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, default="general", null=False)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
