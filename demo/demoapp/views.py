from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    return HttpResponse("Welcome")


def intro(req):
    return HttpResponse("{'hi':'bye'}")


def send_html(req):
    return render(req, 'index.html')

def send_html_dynamic(req):
    return render(req, 'index2.html', {'name':'Sudeep'})

def send_context(req):
    con = [{'name':'sudeep','age':26},
               {'name':'kumar','age':27}]
    context = {'context':con,'np':'npp'}
    return render(req, 'index3.html', context)