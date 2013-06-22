#!/usr/bin/env python
# http://flask.pocoo.org/docs/config/#development-production


class Config(object):
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = True
    PUSHER = dict(APP_ID='<PUSHER APP_ID>',
                  KEY='<PUSHER KEY>',
                  SECRET='<PUSHER SECRET>')
