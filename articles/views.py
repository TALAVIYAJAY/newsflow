from django.shortcuts import render
from django.http import JsonResponse
from .models import NewsArticle

def latest_news(request):
    news = NewsArticle.objects.order_by("-published_at")  # Fetch all articles, latest first
    data = [
        {
            "title": n.title,
            "source": n.source,
            "url": n.url,
            "summary": n.summary,
            "published_at": n.published_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        for n in news
    ]
    return JsonResponse({"articles": data}, safe=False)  # Wrap in "articles" key for structure

def homepage(request):
    articles = NewsArticle.objects.order_by("-published_at")  # Fetch all articles, latest first
    return render(request, "index.html", {"articles": articles})

