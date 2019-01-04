#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2018-12-04

import cv2

img = cv2.imread("/Users/megolees/Documents/screencap.png")

cv2.imshow("img",img)

cv2.waitKey(0)

cv2.destroyAllWindows()