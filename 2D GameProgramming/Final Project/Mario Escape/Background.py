from pico2d import *
import Image

class Background:
    def __init__(self, file):
        self.image = Image.load(file)
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.rect = 0, 0, self.cw, self.ch

    def draw(self):
        self.image.clip_draw_to_origin(*self.rect, 0, 0)

    def update(self):
        pass

    def set_rect(self, x, y=0):
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        cw, ch = self.cw, self.ch
        self.rect = x, y, cw, ch