#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-01-07

__all__ = ['NoneImageException', 'ImageSizeException']


class ImageDiffException(Exception):
    pass


class NoneImageException(ImageDiffException):
    pass


class ImageSizeException(ImageDiffException):
    pass
