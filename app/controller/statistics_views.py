# _*_ coding: utf-8 _*_
from flask_restful import Resource
from app.models.statistics import Statistics
from app.forms.statistics_form import statistics_form
from app import db
from sqlalchemy import func


class StatisticsViews(Resource):
    def get(self, action_type):
        arg_type = statistics_form.parse_args()
        query = db.session.query(Statistics.id, Statistics.date, Statistics.year, Statistics.month, Statistics.day,
                                 func.sum(Statistics.count).label('count'), Statistics.action).select_from(Statistics)
        if action_type == 'register':
            query = query.filter(Statistics.action.in_(['register:ios', 'register:android']))

        elif action_type == 'order_total':
            pass
        elif action_type == 'order_price':
            pass

        if arg_type['type'] == 'year':
            pass
        elif arg_type['type'] == 'month':
            pass
        else:
            ret = query.group_by(Statistics.year, Statistics.month, Statistics.day, Statistics.action).all()

        data, days = [], []
        for item in ret:
            days_key = item.year if arg_type['type'] == 'year' else '%s-%s' % (item.year, item.month)
            days_key = '%s-%s' % (days_key, item.day) if arg_type['type'] == 'day' or not arg_type['type'] else days_key

            data.append(days_key) if not days or days_key != days[-1] else None
            day_data = []
            day_data.append({'name': u'苹果', 'data': int(item.count)}) if item.action == 'register:ios' else \
                day_data.append({'name': u'安卓', 'data': int(item.count)}) if item.action == 'register:android' else None
            days.append(day_data)

            print(item.id, item.action, item.date, item.count)
        data = {"status": True,
                "message": '',
                "data": {
                        "data": data,
                        "days": days
                    }
                }
        print(data)
        return data
