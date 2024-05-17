from django import forms
from solicitacao.models import Solicitacao
from django.core.exceptions import ValidationError
from datetime import date

class SolicitacaoCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    data = forms.DateField(
        initial=date.today,
        widget=forms.TextInput(
            attrs={
                'class':'hide',
                'type':'hidden'
            }
        )
    )

    class Meta:
        model = Solicitacao
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(
                attrs={
                    'class':'hide',
                    'type':'hidden'
                }
            ),
            'status':forms.Select(
                attrs={
                    'class':'hide',
                    'label':'Status'
                }
            ),
            'motivo':forms.Textarea(
                attrs={
                    'placeholder':'Motivo'
                }
            )
        }
        error_messages = {
            'group':{
                'required':'O tipo de nível de acesso é necessário'
            }
        }

        def clean_group(self):
            data = self.cleaned_data.get('group')

            if data is None:
                raise ValidationError(
                    'O tipo de nível de acesso é necessário', code='required'
                )
