from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name="profile"),
    path('new/', views.UserCreateView.as_view(), name = "singup")
]
