from django.urls import  path, include

from rest_framework import routers

from .views import (
    CustomUserViewSet,
    BarberViewSet,
    ProfessionListAPIView,
    DistrictListAPIView,
    LanguageListAPIView,
    PortfolioViewSet,
)

router = routers.DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'barbers', BarberViewSet, basename='barbers')
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns = [
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('profession/', ProfessionListAPIView.as_view()),
    path('district/', DistrictListAPIView.as_view()),
    path('language/', LanguageListAPIView.as_view()),
]

urlpatterns += router.urls
