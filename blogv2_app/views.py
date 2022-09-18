from django.shortcuts import render, redirect, HttpResponse
from .models import Article
from .forms import UpdateForm, AddArticleForm
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def ArticlesView(request):

    articles = Article.objects.filter(status='published').order_by('-id')
    context = {'articles': articles}
    return render(request, 'blogv2_app/html/articles.html', context)
    ordering = ['-date']

@login_required
def ArticleView(request, pk):

    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'blogv2_app/html/article.html', context)


# class UpdateArticleView(UpdateView):
#     model = Article
#     form = UpdateForm
#     form_class = form
#     template_name = "blogv2_app/html/update.html"


def UpdateArticleView(request, pk):
    form = UpdateForm(request.POST or None)
    article = Article.objects.get(pk=pk)
    if form.is_valid() or form != None:
        try:
            title = form.cleaned_data.get("title")
            page_title = form.cleaned_data.get("page_title")
            content = form.cleaned_data.get("content")
            sum = form.cleaned_data.get("sum")
            status = form.cleaned_data.get("status")
  
            article.title = title
            article.page_title = page_title
            article.content = content
            article.sum = sum
            article.status = status

            article.save()
            return redirect(f"http://127.0.0.1:8000/article/{pk}/")
        except:
            pass
            # return HttpResponse("form is none")
        context = {'title': article.title, 'pg_title': article.page_title, 'content': article.content, 'sum': article.sum}
    return render(request, "blogv2_app/html/update.html", context)


class DeleteView(DeleteView):
    model = Article
    template_name = "blogv2_app/html/delete.html"
    success_url = "http://127.0.0.1:8000/"

@login_required
def AddArticleView(request, *args, **kwargs):
    user = request.user
    form = AddArticleForm(request.POST or None)
    if form.is_valid() and form != None:
    
#           FETCHING THE DATA FROM THE FORM

        title = form.cleaned_data.get("title")
        page_title = form.cleaned_data.get("page_title")
        content = form.cleaned_data.get("content")
        status = form.cleaned_data.get("status")
        sum = form.cleaned_data.get("sum")

#           CREATING A NEW ARTICLE WITH THE DATA

        article = Article.objects.create(title=title, page_title=page_title,author=user, content=content, sum=sum, status=status)
        article.save()
        return redirect(f"http://127.0.0.1:8000/article/{article.pk}/")

    context = {'user': user}
    return render(request, "blogv2_app/html/add-article.html", context)

@login_required
def MyArticlesView(request, *args, **kwargs):
    my_articles = Article.objects.filter(author=request.user).order_by('-id')

    context = {'articles': my_articles}
    return render(request, "blogv2_app/html/myarticles.html", context)




