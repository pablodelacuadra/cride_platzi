from django.db import models

from cride.utils.models import CRideModel


class Circle(CRideModel):
    """ Circle model.

        A circle model is a private group where rides are offered and taken by
        its members. To join a circle a user must be receive an unique invitation
        code from a existing circle member.
    """

    name = models.CharField('Circle Name', max_length=150)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('Circle Description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    #Stats

    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    is_verified = models.BooleanField(
        'Verified Circle', 
        default=False,
        help_text='Verified circles are also known as official community'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everybody known about their existence'
    )

    is_limited = models.BooleanField(
        default=False,
        help_text='Limited circles can grow up to fixed number of numbers'
    )
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit on the number of members'
    )

    def __str__(self):
        return self.name
    
    class Meta(CRideModel.Meta):
        ordering = ('-rides_taken', '-rides_offered')
    
    


