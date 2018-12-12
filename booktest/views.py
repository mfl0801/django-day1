from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
# Create your views here.
def index(request):
    temp = loader.get_template('booktest/index.html')
    context = RequestContext(request, {})
    res_html = temp.render(context)
    return HttpResponse(res_html)