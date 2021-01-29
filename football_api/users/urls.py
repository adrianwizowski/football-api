from django.urls import path

from football_api.users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register')
]
