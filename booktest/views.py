from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo# 导入图书模型类
# Create your views here.
def index(request):
    return render(request, 'booktest/index.html', {'content':'hello world', 'list':list(range(1,10))})


def show_books(request):
    '''显示图书的信息'''
    # 1.通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/show_book.html', {'books':books})

def detail(request, bid):
    '''查询图书关联英雄信息'''
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3.使用模板
    return render(request, 'booktest/detail.html', {'book':book, 'heros':heros})