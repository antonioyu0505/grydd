from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AccessPoint, Company, TimeSlot
from .serializers import AccessPointSerializer, CompanySerializer, TimeSlotSerializer
from .services import AccessPointService

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    @action(methods=['get'], detail=True, url_path='validate-access')
    def validate_access(self, request, pk=None):
        service = AccessPointService(company_id=pk)
        access_point_id = request.query_params.get('access-point', None)
        user_id = request.query_params.get('user', None)
        serializer = service.check_access(user_id=user_id, access_point_id=access_point_id)
        return Response(data=serializer.data)
    
class AccessPointViewSet(viewsets.ModelViewSet):
    queryset = AccessPoint.objects.all()
    serializer_class = AccessPointSerializer
    
class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer