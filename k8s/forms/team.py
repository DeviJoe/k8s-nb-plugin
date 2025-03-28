from django.forms import ModelMultipleChoiceField

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField
from ..models.team import Team

class TeamForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = Team
        fields = ('name', 'hub_url', 'comments')