from django import forms
from em16.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'time', 'round', '' 'group', 'teamHomeAlias', 'teamGuestAlias', 'host']

        widgets = {
            'date': forms.SelectDateWidget(),

        }
