from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    # path("january",views.index),
     path("<int:month>",views.monthly_challenges_by_num),
    #  path("<int:month>",views.monthly_challenges_by_num),
    path("<str:month>",views.monthly_challenge, name="month-challenges")
    ]