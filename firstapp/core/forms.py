from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import *


def string_now():
    now = datetime.now()
    now_string = str(now.year) + "-" + ("0" + str(now.month))[-2:] + "-" + ("0" + str(now.day))[-2:]
    now_string += "T" + ("0" + str(now.hour))[-2:] + ":" + ("0" + str(now.minute))[-2:]
    return now_string


class NewNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_do'].label = "Завершить до"
        self.fields["color_id"].label = "Цвет"
        self.fields["color_id"].empty_label = "Не выбран"

    class Meta:
        model = Note
        fields = ["title", "description", "time_do", "color_id"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={'cols': 60, 'rows': 4, 'class': "form-control"}),
            "time_do": forms.DateTimeInput(attrs={"class": "form-control", "value": string_now(),
                                                  "type": "datetime-local"}),
            "color_id": forms.Select(attrs={"class": "form-select"})
        }

    def clean_time_do(self):
        time_do = self.cleaned_data["time_do"]
        if time_do <= datetime.now():
            raise ValidationError("Время завершения должно быть позже текущего времени")
        return time_do
