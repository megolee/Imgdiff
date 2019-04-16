#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-01-07
import cv2
import numpy
from PIL import Image


class ImageMatch(object):

    _image_src = None
    _image_src_gray = None
    _image_template = None

    def __init__(self, image_src, image_template):
        image_src = image_src.read()
        image_template = image_template.read()
        npimage_src = numpy.fromstring(image_src, numpy.uint8)
        npimage_template = numpy.fromstring(image_template, numpy.uint8)
        self._image_src = cv2.imdecode(npimage_src, cv2.IMREAD_COLOR)
        self._image_src_gray = cv2.imdecode(npimage_src, cv2.IMREAD_COLOR)
        self._image_template = cv2.imdecode(npimage_template, cv2.IMREAD_COLOR)

    def match_image(self):
        height, width, _ = self._image_template.shape
        res = cv2.matchTemplate(self._image_src_gray, self._image_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        cv2.rectangle(self._image_src, top_left, bottom_right, (244, 59, 255), 2)
        return Image.fromarray(numpy.uint8(self._image_src))
