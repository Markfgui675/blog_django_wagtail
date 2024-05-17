from django import forms
import django_filters
from feedback.models import Feedback

class FeedbackFilter(django_filters.FilterSet):
    data = django_filters.DateRangeFilter()
    class Meta:
        model = Feedback
        fields = {
            'titulo':['icontains'], 
            'status':['exact']
        }
