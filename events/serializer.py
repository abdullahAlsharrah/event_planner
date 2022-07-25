from rest_framework import serializers
from .models import Event
# class CreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields= '__all__'
        
# class EventListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Event
#         fields='__all__'

# class EventDetailsSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model=Event
#         fields='__all__'

class EventSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'

class AdvanceEventListSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['id','name','start_date']

