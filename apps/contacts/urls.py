from django.urls import path

from .views import ContactListAPIView


urlpatterns = [
    path('', ContactListAPIView.as_view())
]
