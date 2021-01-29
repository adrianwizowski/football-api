from django.urls import path

from football_api.api.notifications.views import NotificationPostAPIView, NotificationLatestRetrieveAPIView

urlpatterns = [
    path('create/', NotificationPostAPIView.as_view(), name='create_notification'),
    path('<id>/latest/', NotificationLatestRetrieveAPIView.as_view(), name='latest_notification_data')
]