from django.forms.models import fields_for_model
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from .models import Profile
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile.html"

class UserCreateView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    
    def get_success_url(self):
        return reverse('login')
