#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
app.config.from_object('webapp.config.config.DevConfig')
from webapp.indexs import image_index
