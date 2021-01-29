from django.core.exceptions import ValidationError
from rest_framework.fields import ListField, IntegerField
from rest_framework.serializers import ModelSerializer

from football_api.api.notifications.models import Notification


class NotificationSerializer(ModelSerializer):
    teams = ListField(child=IntegerField(), read_only=False, required=True)

    class Meta:
        model = Notification
        read_only_fields = ('id', 'created', 'modified', 'user')
        fields = read_only_fields + ('notification_interval', 'notification_type', 'teams', 'email', 'receiver_url')

    def validate(self, data):
        data = super().validate(data)
        notification_type = data.get('notification_type', None)
        notification_email = data.get('email', None)
        notification_receiver_url = data.get('receiver_url', None)

        if notification_type == Notification.NOTIFICATION_TYPE_EMAIL and not notification_email:
            raise ValidationError(
                {'email': ['This field is required while choosing email notifications.']}
            )
        if notification_type == Notification.NOTIFICATION_TYPE_HTTP and not notification_receiver_url:
            raise ValidationError(
                {'receiver_url': ['This field is required while choosing HTTP notifications.']}
            )

        return data
