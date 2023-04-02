from django.urls import path
from blogapp import views

urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact),
]
