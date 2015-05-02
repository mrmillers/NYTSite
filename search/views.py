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
    n = 20
    maxGeoN = 10
    key = request.GET.get("key", "")
    location = request.GET.get("location", "")
    people = request.GET.get("people", "")
    start_time = request.GET.get("start_time", "")
    end_time = request.GET.get("end_time", "")
    data = function.queryResult(n, key, [location, people, start_time, end_time], 0.5)
    for x in data.keys():
        news = News.objects.get(nid=x)
        score = data[x]['score']
        if location != "" and news.location != "":
            if location.lower().find(news.location.lower()) or news.location.lower().find(location.lower()):
                score += 100
        if people != "" and news.author != "":
            if people.lower().find(news.author.lower()) or news.author.lower().find(people.lower()):
                score += 50
        data[x] = {
            'nid': x,
            'score': score,
            'title': news.title,
            'location': news.location,
            'author': news.author,
            'date': news.news_date,
        }
        if data[x]['location'] == "":
            data[x]['location'] = location
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
    geo = {}
    for x in data:
        if data[x]["location"] in geo:
            geo[data[x]["location"]]["score"] += data[x]["score"]
            #geo[data[x]["location"]]["count"] += 1
        else:
            geo[data[x]["location"]] = {
                "score": data[x]["score"],
                #"count": 1,
            }
    geoList = sorted([{"location": x, "score": geo[x]["score"], "count": 0} for x in geo], key=lambda v: v["score"], reverse=True)[:maxGeoN]
    rank = [data[x] for x in data]
    rank.sort(key=lambda v: v['score'], reverse=True)
    for x in rank:
        maxScore = function.get_cosine(x["location"], geoList[0]["location"])
        maxIndex = 0
        for i in range(1, len(geoList)):
            tmp = function.get_cosine(x["location"], geoList[i]["location"])
            if tmp > maxScore:
                maxScore = tmp
                maxIndex = i
        x["geoIndex"] = maxIndex
        geoList[maxIndex]["count"] += 1
    geoNZ = []
    for x in geoList:
        if x['count'] > 0:
            geoNZ.append(x)
    return JsonResponse({"rank": rank, "geo": geoNZ}, safe=False)


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


