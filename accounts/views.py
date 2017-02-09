from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy


User = get_user_model()

class RegisterView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'account/register.html'
    success_url = reverse_lazy('account.login')


register = RegisterView.as_view()
