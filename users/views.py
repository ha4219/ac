from django.views import View
from django.views.generic import FormView, DetailView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from . import forms, models
from django.contrib import messages


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('core:home')
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    # def post(self, request):
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request, username=email, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect(reverse('core:home'))
    #     return render(request, 'users/login.html', {'form': form})
    
def log_out(request):
    messages.info(request, f"See you later")
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('core:home')
    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)
    

def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_scret=key)
        user.email_verified = True
        user.email_secret = ''
        user.save()
    except models.User.DoesNotExist:
        pass
    return redirect(reverse('core:home'))


class UserProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"
    
    
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
        