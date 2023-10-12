from app_resendsrefac.models import Adress
from app_resendsrefac.models import Resident

from rest_framework import serializers

class AdressSerializer(serializers.ModelSerializer):

    class meta:
        model=Adress
        fields='__all__'


class ResidentSerializer(serializers.ModelSerializer):

    class meta:
        model=Resident
        fields='__all__'

