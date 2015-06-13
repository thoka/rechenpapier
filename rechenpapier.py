#!/usr/bin/python2
# encoding: utf8
from __future__ import division

import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm,mm
from math import *
from reportlab.lib.colors import *

def rect(c,x1,y1,x2,y2):
    p = c.beginPath()
    p.moveTo(x1,y1)
    for x,y in [(x2,y1),(x2,y2),(x1,y2)]:
        p.lineTo(x,y)
    p.close()
    return p

def grid(c,nx=50,ny=70,d = 4*mm):

    def set_width(i):
        if i % 10 == 0:
            c.setLineWidth(1.3*mm)
        elif i % 5 == 0:
            c.setLineWidth(0.5*mm)
        else:
            c.setLineWidth(0.1*mm)

    clipp_rect = rect(c,0,0,d*nx,d*ny)
    c.setLineWidth(0.1*mm)
    c.setStrokeColor(white)
    c.clipPath(clipp_rect)

    c.setStrokeColor(black)
    for i in range(ny+1):
        set_width(i)
        c.line(0,i*d,nx*d,i*d) #x
    for i in range(nx+1):
        set_width(i)
        c.line(i*d,0,i*d,ny*d) #y

    c.setStrokeColor(white)
    c.setLineWidth(0.3*mm)
    for i in range(ny+1):
        if i % 10 == 0:
            c.line(0,i*d,nx*d,i*d) #x
    for i in range(nx+1):
        if i % 10 == 0:
            c.line(i*d,0,i*d,ny*d) #y

    if 0:
        c.setStrokeColor(red)
        c.setLineWidth(1*mm)
        c.drawPath(clipp_rect)

c = canvas.Canvas("rechenpapier.pdf",pagesize=A4)

c.translate(0.5*cm,1*cm)
grid(c,nx=50,ny=70,d=4*mm)
c.showPage()

c.translate(0.5*cm,1.5*cm)
grid(c,nx=20,ny=20,d=10*mm)
c.showPage()

c.translate(0.5*cm,1.5*cm)
grid(c,nx=15,ny=15,d=12.54*mm)
c.showPage()

c.translate(0.5*cm,5*cm)
grid(c,nx=10,ny=10,d=20*mm)
c.showPage()

c.save()
