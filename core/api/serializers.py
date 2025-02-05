from models.models import *
from rest_framework import serializers

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    position_id = PositionSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    main_employee = EmployeeSerializer()
    date_since = serializers.DateTimeField(format='%d.%m.%Y')
    class Meta:
        model = Event
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y')
    class Meta:
        model = News
        fields = '__all__'