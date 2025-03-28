from rest_framework import serializers
from virtualization.api.serializers import ClusterSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Team, Namespace

class TeamSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:k8s-api:team-detail',
    )
    class Meta:
        model = Team
        fields = ('id', 'url', 'display', 'name', 'hub_url', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',)


class NestedTeamSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:k8s-api:team-detail',
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'hub_url')


class NamespaceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:k8s-api:namespace-detail',
    )
    cluster = ClusterSerializer()
    team = NestedTeamSerializer()

    class Meta:
        model = Namespace
        fields = ('id', 'url', 'display', 'name', 'cluster', 'team', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',)