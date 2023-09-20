from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        barber = serializer.validated_data['barber']
        existing_rating = Review.objects.filter(user=user, barber=barber).exists()

        if existing_rating:
            return Response({"detail": "You have already voted for this barber."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=user, barber=barber)
