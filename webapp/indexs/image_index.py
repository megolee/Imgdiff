#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from io import BytesIO

from flask import render_template, request
from webapp import app
from webapp.img.imgdiff import ImageDiff
from webapp.exceptions.imagediff_exception import *
from webapp.img.imgmatch import ImageMatch


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def image_diff():
    if request.method == 'GET':
        return render_template('imgdiff.html', message="")
    else:
        img1 = request.files['img1']
        img2 = request.files['img2']
        target = request.form['find']
        try:
            if target == 'findMatch':
                img = ImageMatch(img1, img2).match_image()
            else:
                img = ImageDiff(img1, img2).diff()
            bytes_io = BytesIO()
            img.save(bytes_io, format='PNG')
            return render_template('image.html', image=base64.b64encode(bytes_io.getvalue()).decode('ascii'))
        except NoneImageException:
            return render_template('imgdiff.html', message="NoneImageException")
        except ImageSizeException:
            return render_template('imgdiff.html', message="The size of images are not match")

