#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

from webapp import image_index