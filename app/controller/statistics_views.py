# _*_ coding: utf-8 _*_
from flask_restful import Resource
from app.models.statistics import Statistics
from app.forms.statistics_form import statistics_form
from app import db
from sqlalchemy import func
from runserver import auth
from app.models.order import Order


class StatisticsRegisterViews(Resource):
    @auth.login_required
    def get(self):
        arg_type = statistics_form.parse_args()
        query = db.session.query(Statistics.id, Statistics.date, Statistics.year, Statistics.month, Statistics.day,
                                 func.sum(Statistics.count).label('count'), Statistics.action).select_from(Statistics) \
            .filter(Statistics.action.in_(['register:ios', 'register:android'])) \
            .order_by(Statistics.date.desc())

        group_li = (Statistics.year, Statistics.month, Statistics.day)
        group_li = group_li[:1] if arg_type['type'] == 'year' else group_li[:2] if arg_type['type'] == 'month' else group_li
        for group in group_li:
            query = query.group_by(group)
        ret = query.group_by(Statistics.action).all()

        data, days = [{'name': u'苹果', 'data': []}, {'name': u'安卓', 'data': []}, ], []
        for item in ret:
            date_str = str(item.date)
            days_key = date_str[:4] if arg_type['type'] == 'year' else date_str[:7] if arg_type['type'] == 'month' else date_str[:10]

            if not days or days_key != days[-1]:
                days.append(days_key)
                if item.action == 'register:ios':
                    data[0]['data'].append(int(item.count))
                    data[1]['data'].append(0)
                elif item.action == 'register:android':
                    data[0]['data'].append(0)
                    data[1]['data'].append(int(item.count))
            elif days_key == days[-1]:
                data[0]['data'][-1] += int(item.count) if item.action == 'register:ios' else 0
                data[1]['data'][-1] += int(item.count) if item.action == 'register:android' else 0

        data = {"status": True, "message": '', "data": {"data": data, "days": days}}
        return data


class StatisticsOrderTotalViews(Resource):
    @auth.login_required
    def get(self):
        arg_type = statistics_form.parse_args()
        start, end = (1, 4) if arg_type['type'] == 'year' else (1, 7) if arg_type['type'] == 'month' else (1, 10)

        first_order = db.session.query(Statistics.date, func.substr(Statistics.date, start, end).label('date'),
                                       func.count(1).label('count')).select_from(Statistics). \
            filter(Statistics.action == 'first_order'). \
            order_by(Statistics.date.asc()). \
            group_by(func.substr(Statistics.date, start, end)).all()

        orders = db.session.query(func.substr(Order.created_at, start, end).label('date'),
                                  func.count(1).label('count')).select_from(Order). \
            filter(Order.is_payed == '1'). \
            order_by(Order.created_at.desc()). \
            group_by(func.substr(Order.created_at, start, end)).all()

        data, days = [{'name': u'首单数量', 'data': []}, {'name': u'总订单数', 'data': []}, ], []
        for item in orders:
            days_key = item.date[:end]
            flag = 0
            for i in first_order:
                if days_key == i.date:
                    flag = i.count
            data[0]['data'].append(flag)
            data[1]['data'].append(item.count)
            days.append(days_key)
        data = {"status": True, "message": '', "data": {"data": data, "days": days}}
        return data


class StatisticsOrderPriceViews(Resource):
    @auth.login_required
    def get(self):
        arg_type = statistics_form.parse_args()
        start, end = (1, 4) if arg_type['type'] == 'year' else (1, 7) if arg_type['type'] == 'month' else (1, 10)

        orders = db.session.query(func.substr(Order.created_at, start, end).label('date'),
                                  func.sum(Order.total).label('total'),
                                  func.sum(Order.origin_total).label('origin_total')
                                  ).select_from(Order). \
            filter(Order.is_payed == True). \
            order_by(Order.created_at.desc()). \
            group_by(func.substr(Order.created_at, start, end)).all()

        cancel_orders = db.session.query(func.substr(Order.created_at, start, end).label('date'),
                                         func.sum(Order.origin_total).label('origin_total')).select_from(Order). \
            filter(Order.is_payed == True, Order.status == Order.STATUS_BUYER_CANCEL). \
            order_by(Order.created_at.desc()). \
            group_by(func.substr(Order.created_at, start, end)).all()

        data, days = [{'name': u'销售总额', 'data': []}, {'name': u'支付总额', 'data': []}, {'name': u'退货总额', 'data': []}], []
        for order in orders:
            days_key = order.date[:end]
            flag = 0
            for i in cancel_orders:
                if days_key == i.date:
                    flag = i.origin_total
            data[0]['data'].append(order.origin_total)
            data[1]['data'].append(order.total)
            data[2]['data'].append(flag)
            days.append(days_key)
        data = {"status": True, "message": '', "data": {"data": data, "days": days}}
        return data
