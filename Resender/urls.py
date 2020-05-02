from django.urls import path

from .views import Base, OutputMessagesBase, Button


urlpatterns = [
    path('set-count/', Base.as_view(), name='base'),
    path('', OutputMessagesBase.as_view(),
         name='default_count_messages'),
    path('button', Button.as_view(), name='button_url')
]
