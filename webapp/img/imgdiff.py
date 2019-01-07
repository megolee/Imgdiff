#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
from PIL import Image, ImageColor, ImageChops
from webapp.exceptions.imagediff_exception import *


class ImageDiff(object):
    _imageA = None
    _imageB = None

    # 实例化ImageDiff对象是先检查图片是否存在再判断两张图片大小是否一致
    def __init__(self, imagea, imageb):
        try:
            self._imageA = Image.open(imagea).convert("RGB")
            self._imageB = Image.open(imageb).convert("RGB")
        except FileNotFoundError:
            raise NoneImageException()
        self._verify_image()

    # 判断两张图片大小是否一致
    def _verify_image(self):
        if self._imageA.size != self._imageB.size:
            raise ImageSizeException()

    # 比较图片并返回结果，返回的结果为一张图片；
    # 左边为传入的第一张图，右边为传入的第二张图片，中间是对比图片
    def diff(self):
        """
        :return:  The compare image
        """
        # Step1: ImageChops.difference方法可以比较两张图片的不同并返回图片
        diff_image = ImageChops.difference(self._imageA, self._imageB).convert("L")

        # Step2: 使用Numpy模块找到图片中颜色不是0的所有像素点
        diff_point = numpy.asarray(diff_image)
        diff_point_list = numpy.nonzero(diff_point != 0)
        zip_diff = list(zip(diff_point_list[1], diff_point_list[0]))
        diff_point_list = list(set(zip_diff))

        # Step3: 创建一张透明图片，并将步骤2中找到的像素点的RGB改成(244, 59, 255)
        middle_img = Image.new('RGBA', (self._imageA.width, self._imageA.height), ImageColor.getrgb("#000000"))
        middle_img.putalpha(50)
        for x in diff_point_list:
            middle_img.putpixel(x, (244, 59, 255))

        # Step4： 创建一张大图，左边贴入第一张图，右边贴入第二张图片
        new_image = Image.new('RGBA', (self._imageA.width * 3, self._imageA.height), ImageColor.getrgb("#FFFFFF"))
        new_image.paste(self._imageA)
        new_image.paste(self._imageB, (self._imageB.width * 2, 0))

        # Step5：将透明图和第一张图重叠，然后贴入大图的中间
        r, g, b, a = middle_img.split()
        self._imageA.paste(middle_img, mask=a)
        new_image.paste(self._imageA, (middle_img.width, 0))

        return new_image