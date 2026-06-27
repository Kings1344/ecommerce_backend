from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView

urlpatterns = [
    # Custom Register (your own view)
    path('register/', RegisterView.as_view(), name='register'),

    # JWT Login (using SimpleJWT - recommended)
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Token Refresh
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', ProfileView.as_view()),
]