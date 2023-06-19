from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'resetpassword.html'),name='reset_password' ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'resetpasswordsent.html'),name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'passwordset.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'passwordresetcomplete.html'), name = 'password_reset_complete'),
]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)