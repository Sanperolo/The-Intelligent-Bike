from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, SensorValuesSerializer
from .models import SensorValues

class SensorValuesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SensorValues.objects.all().order_by('-date')
    serializer_class = SensorValuesSerializer

    @action(detail=False, methods=['get'])
    def rain(self, request):
        data = SensorValues.objects.all().values('date', 'raining')
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def humidity(self, request):
        data = SensorValues.objects.all().values('date', 'humidity')
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def temp(self, request):
        data = SensorValues.objects.all().values('date', 'temperature')
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def chart_humidity(self, request):
        data = {}
        data.update({'values': [round(humi_value['humidity'], 2) for humi_value  in SensorValues.objects.all().values('humidity')]}) 
        data.update({'dates': [str(date_value['date'])[11:19] for date_value  in SensorValues.objects.all().values('date')]}) 

        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def chart_temp(self, request):
        data = {}
        data.update({'values': [round(temp_value['temperature'], 2) for temp_value  in SensorValues.objects.all().values('temperature')]}) 
        data.update({'dates': [str(date_value['date'])[11:19] for date_value  in SensorValues.objects.all().values('date')]}) 
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def action_raining(self, request):
        data = {'value': SensorValues.objects.last().raining}
        return Response(data, status=status.HTTP_200_OK)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer