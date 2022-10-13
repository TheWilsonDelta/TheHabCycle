from django.contrib import admin

from . import models


# Register your models here.

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ProgressAdmin(admin.ModelAdmin):
    list_display = ("elevation",)


admin.site.register(models.ToDoList, ToDoListAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Progress, ProgressAdmin)
