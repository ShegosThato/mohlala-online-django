from django.urls import path
from .views import SignUpView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]
