from django_filters import rest_framework as filters
from django_filters import CharFilter
from .models import MainDesc
from django.db import models


class FoodFilter(filters.FilterSet):
    class Meta:
        model = MainDesc
        fields = ['food_code', 'main_food_description']
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }
