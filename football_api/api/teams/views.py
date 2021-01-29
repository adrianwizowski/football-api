import requests

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from football_api.settings import FOOTBALL_DATA_COMPETITION_ID, FOOTBALL_DATA_TOKEN


class ListTeamsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def get(self, request):
        football_data_teams_url = f'http://api.football-data.org/v2/competitions/{FOOTBALL_DATA_COMPETITION_ID}/teams'
        football_data_response = requests.get(football_data_teams_url, headers={'X-Auth-Token': FOOTBALL_DATA_TOKEN})
        return Response(football_data_response.json(), status=football_data_response.status_code)
