from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from virtualization.models import Cluster
from ..models.namespace import Namespace, Team

class NamespaceForm(NetBoxModelForm):

    cluster = DynamicModelChoiceField(
        label="Cluster",
        queryset=Cluster.objects.all(),
        quick_add=True,
    )

    team = DynamicModelChoiceField(
        label="Team",
        queryset=Team.objects.all(),
        quick_add=True,
    )

    comments = CommentField()

    class Meta:
        model = Namespace
        fields = ('name', 'cluster', 'team', 'comments')