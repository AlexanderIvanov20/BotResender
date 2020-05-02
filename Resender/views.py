from django.shortcuts import redirect, render
from django.views import View

from .models import MessageChannel
from .forms import CountMessagesForm

import json


class Base(View):
    def get(self, request):
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        form = CountMessagesForm(initial={'count': data['count_messages']})

        context = {
            'form': form,
            'is_button': data['button']
        }
        return render(request, 'new_index1.html', context)

    def post(self, request):
        form = CountMessagesForm(request.POST)

        if form.is_valid():
            count = form.cleaned_data['count']

            with open('config.json', 'w', encoding='utf-8') as file:
                json.dump({'count_messages': count}, file,
                          indent=4, ensure_ascii=True)

            return redirect('default_count_messages')

        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        context = {
            'form': form,
            'is_button': data['button']
        }
        return render(request, 'new_index1.html', context)


class OutputMessagesBase(View):
    def get(self, request):
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        count = data['count_messages']
        all_messages = MessageChannel.objects.all()[:count][::-1]
        context = {
            'messages': all_messages,
            'is_button': data['button']
        }
        return render(request, 'new_index.html', context)


class Button(View):
    def get(self, request):
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            if data['button'] is True:
                data['button'] = False
            else:
                data['button'] = True

        with open('config.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect('base')
