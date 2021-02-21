"""nbaPlayers serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from nba.models import nbaPlayer


class nbaPlayerModelSerializer(serializers.ModelSerializer):
    """nbaPlayer model serializer."""

    class Meta:
        """Meta class."""
        model = nbaPlayer
        fields = '__all__'
