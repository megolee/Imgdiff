#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2018-11-30


class Config(object):
    DEBUG = False
    SECRET_KEY = 'My flask secret key'


class DevConfig(Config):
    DEBUG = True
