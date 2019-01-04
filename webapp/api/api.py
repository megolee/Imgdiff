#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2018-12-03
from flask_restful import Resource
from webapp import api


class ImageDiffApi(Resource):

    def get(self):
        return {"hello": 'world'}, {"Content-Type": "application/json;charset=UTF-8"}
