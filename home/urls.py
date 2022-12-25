Naziya = "naziya"
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('Mathsolver', views.mathsolver, name='mathsolver'),
    path('mathsolver', views.mathsolver, name='mathsolver'),
    path('homepage', views.homepage, name='home'),
    path('Homepage', views.homepage, name='home'),
    path('Standarddeviation', views.standarddev, name='standarddev'),
    path('standarddeviation', views.standarddev, name='standarddev'),
    path('mean', views.mean, name='mean'),
    path('Mean', views.mean, name='mean'),
    path('median', views.median, name='median'),
    path('Median', views.median, name='median'),
    path('mode', views.mode, name='mode'),
    path('Mode', views.mode, name='mode'),
    path('html', views.html, name='html'),
    path('Html', views.html, name='Html'),
    path('ContactForm', views.contactform, name='contactform'),
    path('contactform', views.contactform, name='contactform'),
    path('range', views.mathsrange, name='range'),
    path('Range', views.mathsrange, name='range'),
    path('quartile', views.quartile, name='quartile'),
    path('Quartile', views.quartile, name='quartile'),
    path('MeanDeviation', views.MeanDeviation, name='meanDeviation'),
    path('meandeviation', views.MeanDeviation, name='meanDeviation'),
    path('About', views.about, name='about'),
    path('about', views.about, name='about'),
    path('Heartlink', views.heartlink, name='heartlink'),
    path('heartlink', views.heartlink, name='heartlink'),
    path('CombinedMean', views.combinedmean, name='combinedmean'),
    path('combinedmean', views.combinedmean, name='combinedmean'),
    path('Combinedmean', views.combinedmean, name='combinedmean'),
]