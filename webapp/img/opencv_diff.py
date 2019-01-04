#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-01-04
import cv2
import numpy


class OpenCVDiff(object):
    _image_height = None
    _image_width = None

    def __init__(self, image_1, image_2):
        self._image_1 = cv2.imread(image_1)
        self._image_2 = cv2.imread(image_2)

    def _verify_image(self):
        if isinstance(self._image_1, numpy.ndarray) and isinstance(self._image_1, numpy.ndarray):
            return True
        return False

    def _subtract(self):
        return cv2.subtract(self._image_1, self._image_2)

    def _find_diff(self):
        compared_image = self._subtract()
        self._image_height, self._image_width, _ = compared_image.shape
        print(self._image_height)
        for x in range(0, self._image_height):
            for y in range(0, self._image_width):
                if list(compared_image[x, y]) != [0, 0, 0]:
                    yield (x, y)

    def _draw_white_image(self):
        img = numpy.zeros([1920, 1080, 3], dtype=numpy.uint8)
        img.fill(255)
        diff = self._find_diff()
        while True:
            try:
                t = diff.__next__()
                img[t] = [245, 102, 93]
            except StopIteration:
                break
        cv2.imshow('IMG', img)
        cv2.waitKey(0)
        cv2.destoryAllWindows()

    def show_image(self):

        self._verify_image()
        self._draw_white_image()


if __name__ == '__main__':
    opendiff = OpenCVDiff('/Users/megolees/Downloads/Wechat1.jpeg', '/Users/megolees/Downloads/Wechat2.jpeg')
    opendiff.show_image()
