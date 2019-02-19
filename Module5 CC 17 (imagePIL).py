# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:49:13 2018

@author: aastha
"""
from PIL import Image
img=Image.open("sample.jpg").convert('L')
print(img.format)
img.show()
img.rotate(-90).show()
img.size
