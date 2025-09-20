from django.contrib import admin

# Register your models here.
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    # Передавать поля можно списком или кортежем. Рекомендовано - картеж, так как он занимает меньше памяти.
    list_display = ("id", "title", "watched", "is_published", "category") # Поля для быстрого просмотра
    list_display_links = ("title",) # Кликабельное поля для перехода к редактированию
    list_editable = ("is_published",) # Поле которое можно изменять при быстром просмотре не заходя в редактирование записи
    readonly_fields = ("watched",) # Поля которые админ не может изменять
    list_filter = ("category", "is_published")


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
