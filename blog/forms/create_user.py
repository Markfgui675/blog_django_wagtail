from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    first_name = forms.CharField(
        label='Primeiro nome',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Primeiro nome'
            }
        )
    )

    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Sobrenome'
            }
        )
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username'
            }
        )
    )

    email = forms.CharField(
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'placeholder':'E-mail'
            }
        )
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Senha'
            }
        )
    )

    password2 = forms.CharField(
        label='Repita a senha',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repita a senha'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        help_texts = {
            'email':'O e-mail deve ser válido'
        }
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        password_error = 'As senha devem ser iguais'
        if password != password2:
            raise ValidationError(
                {
                    'password':ValidationError(password_error, code='invalid'),
                    'password2':ValidationError(password_error, code='invalid')
                }
            )
