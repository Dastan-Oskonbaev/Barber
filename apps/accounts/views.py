from rest_framework import viewsets, generics, permissions

from django_filters.rest_framework import DjangoFilterBackend

from .models import CustomUser, Barber, Profession, District, Language, Portfolio, Service
from .permissions import IsOwnerOrReadOnly
from .filters import BarberFilter
from .serializers import (
    CustomUserSerializer,
    CustomUserUpdateSerializer,
    BarberSerializer,
    BarberCreateSerializer,
    ProfessionSerializer,
    DistrictSerializer,
    LanguageSerializer,
    PortfolioSerializer,
    ServiceSerializer,
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = BarberFilter

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


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
