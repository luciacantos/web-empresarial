from . import views

from django.urls import path

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
]
