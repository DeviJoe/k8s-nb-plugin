from django.db import models

from netbox.models import NetBoxModel
from team import Team


class Namespace(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    cluster = models.ForeignKey(
        to='virtualization.Cluster',
        on_delete=models.CASCADE,
        related_name='namespaces',
    )

    team = models.ForeignKey(
        to=Team,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
    )

    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'namespace'
        verbose_name_plural = 'namespaces'
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'cluster'),
                name='%(app_label)s_%(class)s_unique_namespace_group_name'
            )
        )