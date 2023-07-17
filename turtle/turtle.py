from skimage import io, img_as_float
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import os 
import cv2
import os
from .shell import *
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

class TurtleDPL:
    def paint(self,event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.brush_color)
    def save_drawing(self):
        self.layer.save(f'masks/mask{self.frame}.png')
        self.update_bg_image()
    def change_brush_size(self,val):
        self.brush_size = int(val)
    def update_bg_image(self):
        if self.frame == 0:
            self.frame += 1
        else:
            self.frame += 1
            nextframe = self.frame - 1
            if compare_images(f"frames/frame{nextframe}.jpg",f"frames/frame{self.frame}.jpg"):
                self.frame += 1
            else:
                pass
        self.window.destroy()
        self.__init__(self.frame)
        self.main()
    def __init__(self,frame):
        self.window = tk.Tk()
        self.frame = frame
        self.bg_image = Image.open(f'frames/frame{self.frame}.jpg')        
        self.photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas = tk.Canvas(self.window, width=self.bg_image.width, height=self.bg_image.height)
        self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
        self.canvas.pack()
        self.brush_color = 'black'
        self.brush_size = 5
        self.layer = Image.new('RGBA', self.bg_image.size, (0, 0, 0, 0))
        self.brush_size_slider = tk.Scale(self.window, from_=1, to=50, orient='horizontal', command=self.change_brush_size)
        self.draw = ImageDraw.Draw(self.layer)
        self.brush_size_slider.pack()
        self.save_button = tk.Button(self.window, text='Save drawing', command=self.save_drawing)
        self.save_button.pack()

    def main(self):
        self.canvas.bind("<B1-Motion>", self.paint)
        self.window.mainloop()
    
turt = TurtleDPL(0)
turt.main()
