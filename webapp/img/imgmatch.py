#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-01-07
import cv2


class ImageMatch(object):

    _image_src = None
    _image_src_gray = None
    _image_template = None

    def __init__(self, image_src, image_template):
        self._image_src = cv2.imread(image_src)
        self._image_src_gray = cv2.imread(image_src, 0)
        self._image_template = cv2.imread(image_template, 0)

    def match_image(self):
        height, width = self._image_template.shape
        res = cv2.matchTemplate(self._image_src_gray, self._image_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        cv2.rectangle(self._image_src, top_left, bottom_right, (244, 59, 255), 2)
        return self._image_src


if __name__ == '__main__':

    img = ImageMatch('/Users/megolees/Downloads/Match1.png','/Users/megolees/Downloads/Match5.png')
    img = img.match_image()
    cv2.imshow('Img', img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()
