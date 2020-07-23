from rest_framework import serializers
from anabin.models import Institutions

from rest_framework import exceptions

class InstitutionsSerializer(serializers.ModelSerializer):
    """
        Serializer for InstitutionsStats
    """
    class Meta:
        model = Institutions
        fields = '__all__'