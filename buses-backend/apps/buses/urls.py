from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from apps.buses.views.views_buses import BusesViewSet

app_name = "buses"

router = SimpleRouter(trailing_slash=False)
router.register(r'buses', BusesViewSet, basename='buses')


urlpatterns = router.urls