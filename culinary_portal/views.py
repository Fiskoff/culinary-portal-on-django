from django.shortcuts import render

from .models import Category, Post


#  Представление для главной страницы
def get_index(request):
    """Для главной страницы"""
    posts = Post.objects.all()  # SELECT * FROM post
    categories = Category.objects.all()
    context = {
        "title": "Главая страница",
        "posts": posts,
        "categories": categories,
    }
    # Возвращаем запрос пользователя, шаблон и данные для формирования страницы
    return render(request, "cooking/index.html", context)