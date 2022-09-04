from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('This is my first Django project')

def project(request, primary_key, age):
    return HttpResponse('Single project' + ' ' + str(primary_key) + ' ' + str(age))