from django import forms


class CountMessagesForm(forms.Form):
    count = forms.IntegerField(
        min_value=5,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Введите количество сообщений...'
            }
        ),
        label='Количество сообщений'
    )
