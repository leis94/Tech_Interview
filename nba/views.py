""" nbaPlayers views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Serializers
from nba.serializers import nbaPlayerModelSerializer

# Models
from nba.models import nbaPlayer


class nbaPlayersViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    API endpoint that allows nbaPlayers to be viewed or retrieved.
    """
    queryset = nbaPlayer.objects.all().order_by('id')
    serializer_class = nbaPlayerModelSerializer
