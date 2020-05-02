from django import forms


class CountMessagesForm(forms.Form):
    count = forms.IntegerField(
        min_value=5,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Введите количество сообщений...',
                'style': 'width: 500px',
                'class': 'form-control text-dark shadow'
            }
        ),
        label='Количество сообщений'
    )
