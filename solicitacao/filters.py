from django import forms
import django_filters
from solicitacao.models import Solicitacao

class SolicitacaoFilter(django_filters.FilterSet):
    data = django_filters.DateRangeFilter()

    class Meta:
        model = Solicitacao
        fields = ['group','status']

