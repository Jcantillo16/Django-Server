from rest_framework import serializers
from .models import Persona
from .constants import TIPOS_DOCUMENTO


class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

    def validate_tipo_documento(self, value):
        value = value.upper()
        if value not in TIPOS_DOCUMENTO:
            raise serializers.ValidationError("Tipo de documento no valido")
        return value

    def validate_nombres(self, value):
        value = value.upper()
        return value

    def validate_apellidos(self, value):
        value = value.upper()
        return value

    def validate_hobbie(self, value):
        value = value.upper()
        return value

    def validate_documento(self, value):
        value = value.upper()
        return value
