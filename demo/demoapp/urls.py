from django.urls import path
from . import views
from demoapp import views as demoviews

urlpatterns = [
    path('welcome/', views.welcome),
    path('intro/', views.intro),
    path('sendhtml/', views.send_html),
    path('sendhtml2/', views.send_html_dynamic),
    path('sendhtml3/',views.send_context),
    path('don/', demoviews.intro)
]