from rest_framework import routers

from .views import FavoriteViewSet, FavoriteItemViewSet

router = routers.DefaultRouter()

router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_item', FavoriteItemViewSet)

urlpatterns = router.urls
