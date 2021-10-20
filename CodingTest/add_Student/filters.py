import django_filters 
from .models import Lines

class LineFilter(django_filters.FilterSet):
    class Meta:
        model= Lines
        fields = [
            'classroom',
            'level',
            'description'
        ]

