#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from io import BytesIO

from flask import render_template, request, send_file
from webapp import app
from webapp.cmds.imgdiff import ImageDiff


@app.route('/diff', methods=['POST', 'GET'])
def image_diff():
    if request.method == 'GET':
        return render_template('imgdiff.html')
    else:
        img1 = request.files['img1']
        img2 = request.files['img2']
        img = ImageDiff(img1, img2).compare()
        bytes_io = BytesIO()
        img.save(bytes_io, format='PNG')
        return render_template('image.html', image=base64.b64encode(bytes_io.getvalue()).decode('ascii'))

