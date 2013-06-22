#!/usr/bin/env python
# http://flask.pocoo.org/docs/config/#development-production


class Config(object):
    DEBUG = False
    PUSHER = dict(APP_ID='<PUSHER APP_ID>',
                  KEY='<PUSHER KEY>',
                  SECRET='<PUSHER SECRET>')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
