from django.urls import path, include

urlpatterns = [
    path('teams/', include('football_api.api.teams.urls')),
    path('notifications/', include('football_api.api.notifications.urls'))
]
