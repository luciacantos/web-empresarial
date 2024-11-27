from django import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
