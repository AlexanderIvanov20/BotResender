from django.shortcuts import redirect, render
from django.views import View

from .models import MessageChannel
from .forms import CountMessagesForm


class Base(View):
    def get(self, request):
        form = CountMessagesForm()

        context = {
            'form': form
        }
        return render(request, 'index1.html', context)

    def post(self, request):
        form = CountMessagesForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            count = form.cleaned_data['count']
            return redirect('count_messages', count=count)

        context = {
            'form': form
        }
        return render(request, 'index1.html', context)


class OutputMessagesBase(View):
    def get(self, request):
        all_messages = MessageChannel.objects.all()[:20]
        context = {
            'messages': all_messages
        }
        return render(request, 'index.html', context)


class OutputMessages(View):
    def get(self, request, count):
        all_messages = MessageChannel.objects.all()[:count]
        context = {
            'messages': all_messages
        }
        return render(request, 'index.html', context)
