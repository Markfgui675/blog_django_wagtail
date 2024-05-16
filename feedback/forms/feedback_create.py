from django import forms
from datetime import date
from feedback.models import Feedback
from django.core.exceptions import ValidationError

class FeedbackcreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

    data = forms.DateField(
        initial=date.today,
        label='Data',
        widget=forms.TextInput(
            attrs={
                'class':'slug_hide',
                'type':'date'
            }
        )
    )

    slug = forms.CharField(
        label='Slug',
        widget=forms.TextInput(
            attrs={
                'class':'slug_hide_2',
                'label':'Slug',
                'type':'hidden',
                'value':''
            }
        )
    )


    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'status':forms.Select(
                attrs={
                    'class':'slug_hide',
                    'label':'Status'
                }
            ),
            'titulo':forms.TextInput(
                attrs={
                    'placeholder':'Título do feedback'
                }
            ),
            'descricao':forms.Textarea(
                attrs={
                    'placeholder':'Descrição do feedback'
                }
            )
        }
        error_messages = {
            'titulo':{
                'required':'O feedback precisa ter um título',
                'invalid':'O feedback precisa ter um título'
            },
            'descricao':{
                'required':'O feedback precisa ter uma descrição',
                'invalid':'O feedback precisa ter uma descrição'
            }
        }

        def clean_titulo(self):
            data = self.cleaned_data.get('titulo')

            if len(data) <= 2:
                raise ValidationError(
                    'O feedback precisa de um título', code='invalid'
                )

            return data

        def clean_descricao(self):
            data = self.cleaned_data.get('descricao')

            if len(data) <= 0:
                raise ValidationError(
                    'O feedback precisa ter uma descrição', code='invalid'
                )
