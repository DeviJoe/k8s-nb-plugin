from django.urls import path
from views import *
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    path('teams/', TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', TeamView.as_view(), name='team'),
    path('teams/add/', TeamEditView.as_view(), name='team_add'),
    path('teams/<int:pk>/edit/', TeamEditView.as_view(), name='team_edit'),
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),

    path('namespaces/', NamespaceListView.as_view(), name='namespace_list'),
    path('namespaces/<int:pk>/', NamespaceView.as_view(), name='namespace'),
    path('namespaces/<int:pk>/edit/', NamespaceEditView.as_view(), name='namespace_edit'),
    path('namespaces/<int:pk>/delete/', NamespaceDeleteView.as_view(), name='namespace_delete'),
    path('namespaces/add/', NamespaceEditView.as_view(), name='namespace_add'),

    path('teams/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='team_changelog', kwargs={'model': Team}),
    path('namespaces/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='namespace_changelog', kwargs={'model': Namespace}),
)
