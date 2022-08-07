from datetime import datetime, time
from django.db.models import Q, F, QuerySet
from companies.serializers import AccessPointSerializer
from users.models import Profile
from exceptions.models import UnauthorizedAccess
from .models import AccessPoint, TimeSlot
   
class AccessPointService:
    
    def __init__(self, company_id):
        self.company_id = company_id
    
    def check_access(self, user_id: int, access_point_id: int) -> AccessPointSerializer:
        self._belongs_to_company(access_point_id=access_point_id, company_id=self.company_id)
        access_point: AccessPoint = AccessPoint.objects.get(id=access_point_id)
        access = self._validate_permission(user_id=user_id, access_point=access_point)
        return AccessPointSerializer(access_point, context={"access": access})
    
    @staticmethod
    def _belongs_to_company(access_point_id: int, company_id: int):
        qs: QuerySet = AccessPoint.objects.filter(id=access_point_id, company__pk=company_id)
        if not len(qs):
            raise UnauthorizedAccess
    
    @staticmethod
    def _validate_permission(user_id: int, access_point: AccessPoint, current_time: time = datetime.now().time()) -> bool:
        # QuerySet where start time is less than end time
        time_slots_before_midnight: QuerySet = TimeSlot.objects.filter(
            Q(start__lte=F('end')), Q(start__lte=current_time), 
            end__gte=current_time, 
            access_point=access_point, 
            profile__pk=user_id
        )
        
        # QuerySet where start time is greater than end time (for midnight cases)
        time_slots_after_midnight: QuerySet = TimeSlot.objects.filter(
            Q(start__gt=F('end')), 
            Q(start__lte=current_time) | Q(end__gte=current_time), 
            access_point=access_point, 
            profile__pk=user_id
        )
        time_slots = time_slots_before_midnight | time_slots_after_midnight
        
        if not access_point.active:
            raise UnauthorizedAccess
        return len(time_slots) > 0