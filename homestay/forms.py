from dataclasses import field, fields
from django import forms
from homestay.models import Homestay

class HomestayForm(forms.ModelForm):
    class Meta:
        model = Homestay
        fields = '__all__'