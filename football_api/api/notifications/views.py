from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from football_api.api.notifications.serializers import NotificationSerializer


class NotificationPostAPIView(CreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NotificationLatestRetrieveAPIView(RetrieveAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        # TODO: create logic to retrieve latest match results for saved teams
        raise NotImplementedError
