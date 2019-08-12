from django.db import models


class CRideModel(models.Model):
    """ Base Model.

        This class is an abstract model from wich every other model
        will inherit
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

