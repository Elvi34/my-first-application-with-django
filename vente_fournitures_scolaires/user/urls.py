
# users/urls.py
from django.urls import path
from .views import register
from user import views
from .views import CustomLoginView
from .views import inscription

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
   path('inscription/', inscription, name='inscription'),
]



