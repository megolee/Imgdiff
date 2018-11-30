#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Strikingly on 2018-11-28
from functools import wraps
from flask import session, redirect


class LoginDecorate(object):

    def __call__(self, func):
        @wraps(func)
        def wrapped_decorate(*args, **kwargs):
            if session.get('Username'):
                return func(*args, **kwargs)
            else:
                return redirect('/login')

        return wrapped_decorate
