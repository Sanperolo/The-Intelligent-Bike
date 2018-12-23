from django.contrib.auth.models import User, Group
from .models import SensorValues
from rest_framework import serializers


class SensorValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorValues
        fields = ('date', 'raining', 'temperature', 'humidity')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')