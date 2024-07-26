from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    email = forms.CharField(label='Email', widget=forms.EmailInput)
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')


    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2'] 
        labels = {
            'email':'Email',
            'first-name':'Имя',
            'last-name':'Фамилия',
        }




class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=False, label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.CharField(disabled=False, label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class UserPassChageForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль')
    new_password1 = forms.CharField(label='Новый пароль')
    new_password2 = forms.CharField(label='Подтверждение пароля')
