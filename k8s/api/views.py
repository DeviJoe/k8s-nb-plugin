from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import TeamSerializer, NamespaceSerializer


class TeamViewSet(NetBoxModelViewSet):
    queryset = models.Team.objects.prefetch_related('tags')
    serializer_class = TeamSerializer


class NamespaceViewSet(NetBoxModelViewSet):
    queryset = models.Namespace.objects.prefetch_related(
        'cluster', 'team', 'tags'
    )
    serializer_class = NamespaceSerializer
