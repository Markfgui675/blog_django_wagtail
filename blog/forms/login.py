from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite o username'
            }
        )
    )
    pasword = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite a senha'
            }
        )
    )

