from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name="profile"),
    path('profiles/', views.ProfileListView.as_view(), name="profileList"),
    path('new/', views.UserCreateView.as_view(), name = "singup"),
    path('config/user/<int:pk>', views.UserUpdateView.as_view(), name = "userConfig"),
    path('config/profile/<int:pk>', views.ProfileUpdateView.as_view(), name = "profileConfig"),
    path('config/password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/configs/changing_password.html'), name = "change_password"),
    path('config/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/configs/password_change_done.html'), name = "password_change_done"),
    path('config/password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/configs/password_reset.html"), name = "password_reset"),
    
]