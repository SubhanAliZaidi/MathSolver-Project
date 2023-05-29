Naziya = "naziya"
from django.contrib import admin
from django.urls import path
from home import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name='home'),
    path('Mathsolver', views.mathsolver, name='mathsolver'),
    path('mathsolver', views.mathsolver, name='mathsolver'),
    path('home', views.homepage, name='home'),
    path('Home', views.homepage, name='home'),
    path('Mathsolver/StandardDeviation', views.standarddev, name='standarddev'),
    path('Mathsolver/standarddeviation', views.standarddev, name='standarddev'),
    path('Mathsolver/mean', views.mean, name='mean'),
    path('Mathsolver/Mean', views.mean, name='mean'),
    path('Mathsolver/median', views.median, name='median'),
    path('Mathsolver/Median', views.median, name='median'),
    path('Mathsolver/mode', views.mode, name='mode'),
    path('Mathsolver/Mode', views.mode, name='mode'),
    path('html', views.html, name='html'),
    path('Html', views.html, name='Html'),
    path('ContactForm', views.contactform, name='contactform'),
    path('contactform', views.contactform, name='contactform'),
    path('Mathsolver/range', views.mathsrange, name='range'),
    path('Mathsolver/Range', views.mathsrange, name='range'),
    path('Mathsolver/quartile', views.quartile, name='quartile'),
    path('Mathsolver/Quartile', views.quartile, name='quartile'),
    path('Mathsolver/MeanDeviation', views.MeanDeviation, name='meanDeviation'),
    path('Mathsolver/meandeviation', views.MeanDeviation, name='meanDeviation'),
    path('About', views.about, name='about'),
    path('about', views.about, name='about'),
    path('Heartlink', views.heartlink, name='heartlink'),
    path('heartlink', views.heartlink, name='heartlink'),
    path('Mathsolver/CombinedMean', views.combinedmean, name='combinedmean'),
    path('Mathsolver/combinedmean', views.combinedmean, name='combinedmean'),
    path('Mathsolver/Combinedmean', views.combinedmean, name='combinedmean'),
]