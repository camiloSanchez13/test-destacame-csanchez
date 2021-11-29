from rest_framework.routers import SimpleRouter

from apps.routes.views.views_routes import RoutesViewSet

app_name = "routes"

router = SimpleRouter(trailing_slash=False)
router.register(r'routes', RoutesViewSet, basename='routes')


urlpatterns = router.urls