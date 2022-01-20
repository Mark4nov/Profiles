from pyexpat import model
from django.urls import reverse

#Importing django views
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView

# Importing forms
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

#Importing models
from django.contrib.auth.models import User
from .models import Profile

#Importing decorators / Mixins!
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/index.html"
    paginate_by = 5


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile.html"

### Authentication views

class UserCreateView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    
    def get_success_url(self):
        return reverse('login')


### Configs views!

class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = UserUpdateForm
    template_name='accounts/configs/user.html'
    
    def get_success_url(self):
        user_id = self.object.id
        return reverse('accounts:userConfig', kwargs={'pk': user_id})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name='accounts/configs/profile.html'
    
    def get_success_url(self):
        profile_id = self.object.id
        return reverse('accounts:profileConfig', kwargs={'pk': profile_id})

