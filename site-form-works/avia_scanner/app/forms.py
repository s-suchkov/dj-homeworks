from django import forms
from .models import City
from .widgets import AjaxInputWidget
# from app.views import cache_choices
class SearchTicket(forms.Form):
    departure = forms.CharField(
        label='Вылет',
        widget=AjaxInputWidget(
            url='api/city_ajax',
            attrs={'class': 'inline right-margin'}
        )
    )
    arrival = forms.ChoiceField(
        label='Прилет',
        choices=[(x, x) for x in City.objects.all()]
    )
    date = forms.DateField(
        label='Дата',
        # widget=forms.DateInput(attrs={'type':'date'})
        widget=forms.SelectDateWidget
    )
    # Добавьте здесь поля, описанные в задании
    pass
