from django.forms import ModelForm
from .models import Item


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

