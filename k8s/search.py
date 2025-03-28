from netbox.search import SearchIndex, register_search
from models import Team, Namespace

@register_search
class NamespaceIndex(SearchIndex):
    model = Namespace
    fields = (
        ('name', 100),
    )

@register_search
class TeamIndex(SearchIndex):
    model = Team
    fields = (
        ('name', 100),
    )