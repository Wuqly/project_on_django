from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView

from .forms import ProfileUserForm, forms, UserPassChageForm

from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}

"""    def get_success_url(self):
        return reverse('home')"""


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')



class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    extra_context = {'title': 'Профиль'}
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')
    
    def get_object(self, queryset = None):
        return self.request.user
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой Email уже существует')
        return email
    

class UserPasswordChange(PasswordChangeView):
    form_class = UserPassChageForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': 'Изменение пароля'}

