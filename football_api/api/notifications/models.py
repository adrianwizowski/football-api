from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Notification(models.Model):
    """Model containing basic information about created notification."""
    NOTIFICATION_INTERVAL_DAY = 'day'
    NOTIFICATION_INTERVAL_WEEK = 'week'
    NOTIFICATION_INTERVAL_LIVE = 'live'
    NOTIFICATION_TYPE_EMAIL = 'email'
    NOTIFICATION_TYPE_HTTP = 'http'

    INTERVALS = [
        (x, x.capitalize())
        for x in [
            NOTIFICATION_INTERVAL_DAY,
            NOTIFICATION_INTERVAL_WEEK,
            NOTIFICATION_INTERVAL_LIVE
        ]
    ]

    TYPES = [
        (x, x.capitalize())
        for x in [
            NOTIFICATION_TYPE_EMAIL,
            NOTIFICATION_TYPE_HTTP
        ]
    ]

    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=True,)
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.CASCADE,
        null=False,
        related_name='notification_created',
    )
    email = models.EmailField(null=True)
    receiver_url = models.URLField(null=True)
    notification_interval = models.CharField(max_length=32, choices=INTERVALS, null=False)
    notification_type = models.CharField(max_length=32, choices=TYPES, null=False)
    teams = ArrayField(
        models.IntegerField(editable=True, null=False)
    )
