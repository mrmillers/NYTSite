from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from .models import *
import function
# Create your views here.


def index(request):
    return render(request, "search/index.html", {})


def query(request):
    n = 10
    key = request.GET.get("key", "")
    location = request.GET.get("location", "")
    people = request.GET.get("people", "")
    start_time = request.GET.get("start_time", "")
    end_time = request.GET.get("end_time", "")
    data = function.queryResult(n, key, [location, people, start_time, end_time], 1)
    for x in data.keys():
        news = News.objects.get(nid=x)
        score = data[x]['score']
        data[x] = {
            'score': score,
            'title': news.title,
            'location': news.location,
            'author': news.author,
            'date': news.news_date,
        }
    if start_time != "":
        t = function.strToDate(start_time)
        for x in data:
            if data[x]['date'] < t:
                data[x]['score'] -= 100
    if end_time != "":
        t = function.strToDate(end_time)
        for x in data:
            if data[x]['date'] > t:
                data[x]['score'] -= 100
    rank = [data[x] for x in data]
    rank.sort(key=lambda v: v['score'], reverse=True)
    return JsonResponse(rank, safe=False)


def search(request):
    key = request.GET.get("key", "@@")
    return HttpResponse(key)


def advanced_search(request):
    return render(request, "search/advanced_search.html", {})


def map_test(request):
    return render(request, "search/mapTest.html")


def article(request, key):
    try:
        news = News.objects.get(nid=key)
        data = {}
        if news.title != "":
            data["title"] = news.title
        else:
            data["title"] = "New York Times Article"
        if news.author != "":
            data["author"] = news.author
        if news.location != "":
            data["location"] = news.location
        data["date"] = news.news_date
        data["text"] = []
        for s in news.text.split('\n'):
            if s != "":
                data["text"].append(s)
    except:
        raise Http404
    return render(request, "search/article.html", data)