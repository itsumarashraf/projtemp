import django_filters
from criminals.models import criminal
from django import forms


class userfilter(django_filters.FilterSet):
    fname= django_filters.CharFilter(label='Criminal', lookup_expr='icontains')
    class Meta:
        model= criminal
        fields=['fname']