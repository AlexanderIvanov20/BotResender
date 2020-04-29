from django.urls import path

from .views import *


urlpatterns = [
    path('', Base.as_view(), name='base')
]
