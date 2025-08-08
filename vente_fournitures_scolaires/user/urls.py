
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



from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
]
