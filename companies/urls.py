from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet, AccessPointViewSet, TimeSlotViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('access-points', AccessPointViewSet, basename='access-point')
router.register('timeslot', TimeSlotViewSet, basename='timeslot')