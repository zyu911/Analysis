from . import api
from controller import account_views
from controller import histories_views
from controller import statistics_views

api.add_resource(histories_views.HistoriesViews,
                 '/api/v1.0/histories/',
                 '/api/v1.0/histories/<string:id>',
                 endpoint='Histories')
# api.add_resource(account_views.Register, '/api/v1.0/register')
api.add_resource(account_views.Login, '/api/v1.0/login')
api.add_resource(account_views.Logout, '/api/v1.0/logout')
api.add_resource(statistics_views.StatisticsRegisterViews, '/api/v1.0/statistics/register')
api.add_resource(statistics_views.StatisticsOrderTotalViews, '/api/v1.0/statistics/order_total')
api.add_resource(statistics_views.StatisticsOrderPriceViews, '/api/v1.0/statistics/order_price')
