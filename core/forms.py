from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento do nome'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
            }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido'},
        widget=forms.EmailInput(

            attrs={
                "class": "form-control",
                "placeholder": " Your email"
            }
        )
    )
    mensagem = forms.CharField(
        error_messages={'required': 'È obrigatorio o preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua mensagem'
            }
        )
    )


def clean_email(self):
    email = self.cleaned_data['email']
    if not 'gmail' in email:
        raise forms.ValidationError('O email deve ser do gmail.com')
    return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError('Esse usuario já existe, escolha outro nome')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError('Esse email já existe, tente outro')
        return email

    def clean_confirm_password(self):
        data = self.cleaned_data
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('As senhas informadas deve ser iguais')
        return data
