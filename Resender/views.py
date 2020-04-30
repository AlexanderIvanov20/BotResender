from django.shortcuts import render
from django.views import View

from .models import MessageChannel


class Base(View):
    def get(self, request):
        all_messages = MessageChannel.objects.all()[:20]

        for i in all_messages:
            print(i.url)

        context = {
            'messages': all_messages
        }
        return render(request, 'index.html', context)
