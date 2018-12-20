#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from webapp.api.api import ImageDiffApi

app = Flask(__name__)
api = Api(app)
api.add_resource(ImageDiffApi, '/api/imagediff')
app.config.from_object('webapp.config.config.DevConfig')
from webapp.indexs import image_index
