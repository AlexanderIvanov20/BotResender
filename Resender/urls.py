from django.urls import path

from .views import Base, OutputMessagesBase, New


urlpatterns = [
    path('set-count/', Base.as_view(), name='base'),
    path('', OutputMessagesBase.as_view(),
         name='default_count_messages'),
    path('new', New.as_view(), name='new')
]
