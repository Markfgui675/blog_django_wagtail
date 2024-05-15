from django import forms
from blog.models import Email

class EmailForm(forms.ModelForm):

    email = forms.CharField(
        label=None,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Seu e-mail'
            }
        )
    )

    class Meta:
        model = Email
        fields = '__all__'
