from django.contrib.auth import views
from django.urls import path


app_name = 'authentication'


urlpatterns = [
    path('account/logout/', views.LogoutView.as_view(), name='logout'),
    path('account/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('account/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('account/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('account/password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('account/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
