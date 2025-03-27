from netbox.views import generic
from .tables import *
from .forms import *

# Team view
class TeamView(generic.ObjectView):
    queryset = Team.objects.all()

class TeamListView(generic.ObjectListView):
    queryset = Team.objects.all()
    table = TeamTable

class TeamEditView(generic.ObjectEditView):
    queryset = Team.objects.all()
    form = TeamForm

class TeamDeleteView(generic.ObjectDeleteView):
    queryset = Team.objects.all()

# Namespace view
class NamespaceView(generic.ObjectView):
    queryset = Namespace.objects.all()

class NamespaceListView(generic.ObjectListView):
    queryset = Namespace.objects.all()
    table = NamespaceTable

class NamespaceEditView(generic.ObjectEditView):
    queryset = Namespace.objects.all()
    form = NamespaceForm

class NamespaceDeleteView(generic.ObjectDeleteView):
    queryset = Namespace.objects.all()