import django_tables2 as tables

from netbox.tables import NetBoxTable
from ..models import Namespace

class NamespaceTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
    )

    cluster = tables.Column(
        linkify=True,
    )

    team = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Namespace
        fields = ('pk', 'name', 'cluster', 'team', 'actions')
        default_columns = ('name', 'cluster', 'team')