from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

"""
INFO: The reset password email is received in prompt when DEBUG mode is ON.
"""

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('password_reset/Done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/configs/password_reset_done.html'), name = "password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/configs/password_reset_confirm.html'), name = "password_reset_confirm"),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/configs/password_reset_complete.html'), name = "password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
