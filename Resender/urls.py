from django.urls import path

from .views import *


urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('chat/', OutputMessagesBase.as_view(), name='default_count_messages'),
    path('chat/<int:count>/', OutputMessages.as_view(),
         name='count_messages')
]
