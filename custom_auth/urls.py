from django.urls import path

from custom_auth import views


urlpatterns = [
    path('login/', views.login, name='api-login'),
    path('logout/', views.logout, name='api-logout'),
    path('session/', views.session, name='api-session'),
    path('whoami/', views.whoami, name='api-whoami'),
]
