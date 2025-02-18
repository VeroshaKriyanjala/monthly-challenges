from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges={
    "january":"Eat no meat for the entire month",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day!",
    "april":"Eat no meat for the entire month",
    "may":"Walk for at least 20 minutes every day!",
    "june":"Learn Django for at least 20 minutes every day!",
    "july":"Eat no meat for the entire month",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn Django for at least 20 minutes every day!",
    "october":"Eat no meat for the entire month",
    "november":"Walk for at least 20 minutes every day!",
    "december":"Learn to sing for at least 20 minutes every day!"
}

def index(request):
    return HttpResponse("Hello, world. You're at the challenges index.")

def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
    except: 
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

def monthly_challenges_by_num(request, month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month=months[month-1]
    redirect_path=reverse("maonth-challenges",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)