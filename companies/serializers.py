from rest_framework import serializers

from .models import Company, AccessPoint, TimeSlot

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'commercial_name',
            'address',
            'phone_number',
            'email',
            'website',
            'city',
            'admin'
        ]
        
class AccessPointSerializer(serializers.ModelSerializer):
    access = serializers.SerializerMethodField()
    class Meta:
        model = AccessPoint
        fields = [
            'id',
            'name',
            'address',
            'email',
            'active',
            'longitude',
            'latitude',
            'company',
            'access'
        ]
        
    def get_access(self, obj):
        return self.context.get('access')
    
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = [
            'start',
            'end',
            'access_point',
            'profile'
        ]