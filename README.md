# football-api
## Setup
Before starting app please provide following env vars:

```
    POSTGRES_DB_NAME
    POSTGRES_USERNAME
    POSTGRES_PASSWORD
    POSTGRES_HOSTNAME
    POSTGRES_PORT
    FOOTBALL_DATA_TOKEN
    DJANGO_SECRET_KEY
```

`FOOTBALL_DATA_TOKEN` can be obtain by registering at: football-data.org

`DJANGO_SECRET_KEY` can be generated here: https://miniwebtool.com/django-secret-key-generator/

By default app provides results for English Premiere League.
Default league can be changed bu setting `FOOTBALL_DATA_COMPETITION_ID` env var.
List of leagues can be found here: http://api.football-data.org/v2/competitions
API token lifetime is set to 30 minutes by default. 
This can be changed by passing expected lifetime in minutes under a
`JWT_TOKEN_LIFETIME` env var. 


## List of endpoints

    /admin/ - admin site
    /auth/token/ - retrieve token
    /auth/token/refresh/ - refresh token
    /user/register/ - create user
    /api/teams/ - list all teams in a supported league
    /api/notifications/create/ - create user notification
    /api/notifications/<id>/latest/ - get latest data for given notification (not implemented)
    
    
## TODO

 - finish the endpoint for latest notifications
 - create a logic to collect latest data from football-data.org (https://github.com/celery/django-celery-beat)
 - create a logic to send notifications to the users (https://github.com/celery/django-celery-beat)
 - validate list of teams sent by the user against a list of teams in currently supported league
 - add a Swagger documentation
 - add a changelog
 - implement docker
 - add tests