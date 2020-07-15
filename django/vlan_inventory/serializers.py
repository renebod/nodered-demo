from rest_framework import serializers
from .models import VLAN


class VLANSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = VLAN
        fields = ('id', 'name', 'description',)
