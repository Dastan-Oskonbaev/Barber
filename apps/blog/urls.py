from django.urls import path

from .views import CategoryListAPIView, BlogDetailAPIView


urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('<int:pk>/', BlogDetailAPIView.as_view()),
]
