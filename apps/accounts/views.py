from django.shortcuts import render

from rest_framework import viewsets, generics, permissions

from .models import CustomUser, Barber, Profession, District, Language
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CustomUserSerializer,
    CustomUserUpdateSerializer,
    BarberSerializer,
    BarberCreateSerializer,
    ProfessionSerializer,
    DistrictSerializer,
    LanguageSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return CustomUserUpdateSerializer
        return self.serializer_class


class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return BarberCreateSerializer
        return self.serializer_class


class ProfessionListAPIView(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DistrictListAPIView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageListAPIView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
