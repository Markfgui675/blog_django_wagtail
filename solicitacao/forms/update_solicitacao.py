from django import forms
from solicitacao.models import Solicitacao

class SolicitacaoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Solicitacao
        fields = ['status']
