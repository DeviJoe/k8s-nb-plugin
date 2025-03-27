from django.db import models

from netbox.models import NetBoxModel

from django.urls import reverse

class Team(NetBoxModel):
    name = models.CharField(
        verbose_name='name',
        max_length=100,
        unique=True,
    )

    url = models.URLField(
        verbose_name='url',
    )

    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'team'
        verbose_name_plural = 'teams'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:k8s:team', kwargs={'pk': self.pk})