from django.urls import path

from football_api.api.teams.views import ListTeamsAPIView

urlpatterns = [
    path('', ListTeamsAPIView.as_view(), name='list_teams'),

]