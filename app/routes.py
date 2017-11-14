from . import api
from controller import account_views
from controller import histories_views


api.add_resource(histories_views.HistoriesViews,
                 '/api/v1.0/histories/',
                 '/api/v1.0/histories/<string:id>',
                 endpoint='Histories')
api.add_resource(account_views.Users, '/api/v1.0/users/')
# api.add_resource(account_views.Token, '/api/v1.0/token')
