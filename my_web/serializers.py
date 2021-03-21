from .models import case
from rest_framework import serializers
from django.contrib.auth.models import User


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = case
        fields = ('url', 'name', 'module', 'step','result','grade','execution','cover')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class ApiCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')