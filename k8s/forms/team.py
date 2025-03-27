from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField
from ..models.team import Team

class TeamForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = Team
        fields = ('name', 'url', 'comments')