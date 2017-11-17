# -*- coding:utf-8 -*-
from app import db


class Order(db.Model):
    __tablename__ = 'ba_orders'

    PAY_WAITING = 0   # 待支付
    PAY_SUCCESS = 1   # 已支付
    STATUS_WAITING = 1   # 等待付款
    STATUS_DELIVER_WAITING = 2   # 待发货
    STATUS_DELIVER_SUCCESS = 3   # 已发货
    STATUS_DELIVER_PART = 10   # 部分已发货
    STATUS_BUYER_CANCEL = 4   # 买家取消订单
    STATUS_CANCELING = 9   # 买家申请取消订单
    STATUS_OVERTIME_PAYMENT = 5   # 超时未付款
    STATUS_RETURNING = 6   # 退货中
    STATUS_RETURN_SUCCESS = 7   # 退货完成
    STATUS_FINISH = 8   # 订单完成
    CANCEL_STATUS_WAREHOUSE = 1
    CANCEL_STATUS_FINANCE = 2
    CANCEL_STATUS_CEO = 3
    CANCEL_STATUS_END = 4

    user_id = db.Column(db.Integer, primary_key=True)
    order_no = db.Column(db.String(255))
    total = db.Column(db.Float)
    freight = db.Column(db.Integer)
    is_payed = db.Column(db.String(255))
    pay_method = db.Column(db.String(255))
    status = db.Column(db.String(255))
    cancel_status = db.Column(db.Integer)
    origin_total = db.Column(db.Float)
    trade_no = db.Column(db.String(255))
    trade_name = db.Column(db.String(255))
    coupon_number_id = db.Column(db.String(255))
    source = db.Column(db.String(255))
    note = db.Column(db.String(255))
    created_at = db.Column(db.String(30))
    updated_at = db.Column(db.String(30))

    def __repr__(self):
        return '<order %r>' % self.order_no
