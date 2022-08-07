from rest_framework import viewsets

from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.prefetch_related('country')
    serializer_class = StateSerializer
    
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.prefetch_related('state')
    serializer_class = CitySerializer