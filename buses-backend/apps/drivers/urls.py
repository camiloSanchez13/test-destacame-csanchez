from rest_framework.routers import SimpleRouter

from apps.drivers.views.views_drivers import DriversViewSet

app_name = "drivers"

router = SimpleRouter(trailing_slash=False)
router.register(r'drivers', DriversViewSet, basename='drivers')


urlpatterns = router.urls