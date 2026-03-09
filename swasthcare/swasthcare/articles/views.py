from django.shortcuts import render
from .models import Article
from django.http import JsonResponse
import json


def home(request):

    articles = Article.objects.all()

    return render(request,'articles/home.html',{
        'articles':articles
    })


def chat(request):

    data=json.loads(request.body)

    message=data.get("message").lower()

    health_keywords=["diet","fitness","exercise","workout","health","weight","yoga","protein"]

    if any(word in message for word in health_keywords):

        if "diet" in message:
            reply="A balanced diet includes vegetables, fruits, proteins and enough water."

        elif "exercise" in message:
            reply="Try 30 minutes of exercise daily like walking, yoga or light cardio."

        elif "weight" in message:
            reply="Regular exercise and a healthy calorie-controlled diet can help with weight management."

        else:
            reply="Maintaining a healthy lifestyle with good diet and exercise improves overall health."

    else:

        reply="❌ I can only answer questions about health, diet, fitness and lifestyle."

    return JsonResponse({"reply":reply})





