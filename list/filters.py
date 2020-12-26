import django_filters
from .models import Item


class DateFilter(django_filters.FilterSet):

    class Meta:
        model = Item
        fields = ['date_created']
