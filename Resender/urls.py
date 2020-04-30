from django.urls import path

from .views import *


urlpatterns = [
    path('set-count/', Base.as_view(), name='base'),
    path('', OutputMessagesBase.as_view(),
         name='default_count_messages'),
]
