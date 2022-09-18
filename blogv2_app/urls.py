from django.urls import path
from .views import ArticlesView, ArticleView, UpdateArticleView, DeleteView, AddArticleView, MyArticlesView
from django.contrib import admin

urlpatterns = [
    path('', ArticlesView, name='articlesview'),
    path('article/<int:pk>/',ArticleView, name='articleview'),
    # path('article/<int:pk>/update/', UpdateArticleView.as_view(), name='updateview'),
    path('article/<int:pk>/update/', UpdateArticleView, name='updateview'),
    path('article/<int:pk>/delete/', DeleteView.as_view(), name='deleteview'),
    path('articles/add/', AddArticleView, name='addarticleview'),
    path('articles/my-articles/', MyArticlesView, name='myarticlesview')
]