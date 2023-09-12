from django.urls import path

from .views import CityListAPIView, CityDetailAPIView


urlpatterns = [
    path('', CityListAPIView.as_view()),
    path('<int:pk>/', CityDetailAPIView.as_view()),
]
