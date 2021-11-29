from rest_framework.routers import SimpleRouter

from apps.passengers.views.views_passengers import PassengersViewSet

app_name = "passengers"

router = SimpleRouter(trailing_slash=False)
router.register(r'passengers', PassengersViewSet, basename='drivers')


urlpatterns = router.urls