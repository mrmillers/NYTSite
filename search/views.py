from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
	return render(request,"search/index.html",{})

def search(request):
	key = request.GET.get("key","@@")
	location = request.GET.get("location","");
	people = request.GET.get("people","");
	
	return HttpResponse(key)

def advanced_search(request):
	return render(request,"search/advanced_search.html",{})