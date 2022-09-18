
from django.urls import path, include
from .views import RegView, LoginView

urlpatterns = [
    path('register/', RegView, name="regview"),
    path('accounts/login/', LoginView, name='loginview')
]
