from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Review


@receiver(post_save, sender=Review)
def update_barber_average_rating(sender, instance, **kwargs):
    barber = instance.barber
    reviews = Review.objects.filter(barber=barber)
    total_ratings = sum(review.rating for review in reviews)
    num_reviews = reviews.count()

    if num_reviews > 0:
        average_rating = total_ratings / num_reviews
    else:
        average_rating = 0

    barber.average_rating = average_rating
    barber.save()
