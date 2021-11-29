from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from apps.journeys.views.views_journeys import JourneyViewSet
from apps.journeys.views.views_tickets import TicketsViewSet, JourneyTicketViewSet

app_name = "journeys"

router = SimpleRouter(trailing_slash=False)
router.register(r'journeys', JourneyViewSet, basename='journeys')
router.register(r'tickets', TicketsViewSet, basename='tickets')

journey_router = NestedSimpleRouter(router, r'journeys', lookup='journey')
journey_router.register(r'tickets', JourneyTicketViewSet, basename='tickets_journey')

urlpatterns = router.urls + journey_router.urls