from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december":None
}

def index(request):
    list_items=""
    months=list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{
        "months":months
    })


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name": month
        })
    except: 
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

def monthly_challenges_by_num(request, month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenges",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)