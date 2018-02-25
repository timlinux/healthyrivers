# coding=utf-8
"""IUCN Status model definition.

"""

from django.db import models


class IucnStatus(models.Model):
    """IUCN status model."""

    name = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )
    sensitive = models.BooleanField(
        default=False
    )

    def __unicode__(self):
        return u'%s' % self.name
