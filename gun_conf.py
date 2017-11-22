# -*- coding:utf8 -*-
import os
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

debug = True
loglevel = 'debug'
bind = '127.0.0.1:5000'
pidfile = '/tmp/gunicorn.pid'
logfile = '/var/debug.log'

workers = 2
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'
