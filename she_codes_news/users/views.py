  
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ChangeAccountView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'users/changeAccount.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AccountView(DetailView):
    template_name = 'users/viewAccount.html'
    model = CustomUser
    context_object_name = 'user'

class AuthorView(generic.DetailView):
    template_name = 'users/Author.html'
    model = CustomUser
    context_object_name = "author"
