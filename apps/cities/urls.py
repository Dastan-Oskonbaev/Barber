from django.urls import path

from .views import CityDetailAPIView


urlpatterns = [
    path('<int:pk>/', CityDetailAPIView.as_view())
]
