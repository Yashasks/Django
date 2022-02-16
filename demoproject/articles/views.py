from django.shortcuts import render
from .models import Article

# Create your views here.

def article_list(request):
    article = Article.objects.all().order_by('name')
    
    return render(request,'articles/article_list.html', {'article':article})