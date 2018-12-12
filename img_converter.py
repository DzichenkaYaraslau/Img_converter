#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:45:54 2018

@author: botan
"""

from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt

leds = 8
lines = 360
a = np.linspace(0, 2*math.pi, 360, endpoint=False)
img = Image.open("images.png").convert('RGB')
xm = img.size[0]
ym = img.size[1]
#print(xm, ym)
#if xm % 2 == 0:
#    xm += 1
#if ym % 2 == 0:
#    ym += 1
print(xm, ym)
center = [round(xm/2), round(ym/2)]
print(center)
fac = [img.size[0]/(2*leds), img.size[1]/(2*leds)]
for theta in a:
    for i in range(1, leds):
        
        xN = center[0] + round(fac[0]*math.cos(theta)*i)
        yN = center[1] + round(fac[1]*math.sin(theta)*i)
#        print(xN, yN)
#        print()
        plt.plot(xN, yN, (img.getpixel((xN, yN))[0]/255,
                          img.getpixel((xN, yN))[1]/255,
                          img.getpixel((xN, yN))[2]/255))
        plt.xlim(0, 2*leds)
        plt.ylim(0, 2*leds)
#print(a)

#

#

#img_out = Image.new('RGB', [pixels, pixels])
#trX = round(xm/2)
#trY = round(ym/2)
#print(trX, trY)
#aX = round(xm/pixels)
#aY = round(ym/pixels)
#print(aX, aY)
#for x in range(0, xm):
#    
#img_new.save('out.bmp')
#        pixels[xm + 1, y] = (0, 0, 0)
#    print(1)
#    for y in range(ym):
#        pixels[xm + 1, y] = (0, 0, 0)
#a = 10
#img_new = Image.new('RGB', (pixels, pixels))
#img_new.putpixel()
#xm = img.size[0]
#ym = img.size[1]
#for i in range(xm):
#    for j in range(ym):
#        print(img.getpixel((i, j)))
#r, g, b = img.getpixel((100, 200))
#print(r, g, b)