"""Stub implementations for Enterprise Event/Property definitions in FOSS version"""

from posthog.models.event_definition import EventDefinition
from posthog.models.property_definition import PropertyDefinition
from rest_framework import serializers


# Just use the base models as stubs
EnterpriseEventDefinition = EventDefinition
EnterprisePropertyDefinition = PropertyDefinition


class EnterpriseEventDefinitionSerializer(serializers.ModelSerializer):
    """Stub serializer for enterprise event definitions"""
    class Meta:
        model = EventDefinition
        fields = "__all__"


class EnterprisePropertyDefinitionSerializer(serializers.ModelSerializer):
    """Stub serializer for enterprise property definitions"""
    class Meta:
        model = PropertyDefinition
        fields = "__all__"