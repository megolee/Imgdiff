#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageColor, ImageChops


class ImageDiff(object):
    _imageA = None

    _imageB = None

    def __init__(self, imagea, imageb):
        self._imageA = Image.open(imagea).convert("RGB")
        self._imageB = Image.open(imageb).convert("RGB")

    def compare(self):
        imgS = Image.new('RGBA', (self._imageA.width * 3, self._imageB.height), ImageColor.getrgb("#FFFFFF"))
        imgS.paste(self._imageA)
        imgS.paste(self._imageB, (self._imageB.width * 2, 0))

        image = ImageChops.difference(self._imageA, self._imageB)

        image = image.convert("L")

        img = Image.new('RGBA', (image.width, image.height), ImageColor.getrgb("#000000"))
        img.putalpha(100)

        for x in range(0, image.width):
            for y in range(0, image.height):
                pixel = image.getpixel((x, y))
                if pixel != 0:
                    img.putpixel((x, y), (255, 99, 71))

        r, g, b, a = img.split()

        self._imageA.paste(img, mask=a)

        imgS.paste(self._imageA, (image.width, 0))

        return imgS