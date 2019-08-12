from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """ Extends from django abstract user"""

    email = models.EmailField(
        'Email Address',
        unique=True,
        error_messages={
            'unique': ' A user with that email already exists'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +569 12345678.'
    )
    phone_number = models.CharField(
        validators= [phone_regex],
        max_length=17,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'Client Status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Client are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'Verified Status',
        default=False,
        help_text=(
            'Set to true when user verify email address'
        )
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

