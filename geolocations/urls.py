from rest_framework.routers import SimpleRouter
from .views import CountryViewSet, StateViewSet, CityViewSet

router = SimpleRouter()

router.register('countries', CountryViewSet, basename='country')
router.register('states', StateViewSet, basename='state')
router.register('cities', CityViewSet, basename='city')