import django_tables2 as tables

from netbox.tables import NetBoxTable
from ..models import Team

class TeamTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
        verbose_name='Name'
    )

    url = tables.Column(
        linkify=True,
        verbose_name='URL'
    )

    class Meta(NetBoxTable.Meta):
        model = Team
        fields = ('pk', 'name', 'hub_url', 'actions')
        default_columns = ('name', 'hub_url')