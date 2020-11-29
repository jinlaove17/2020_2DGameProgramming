from pico2d import *
import Image

class Background:
    def __init__(self, file, player=None):
        self.image = Image.load(file)
        self.mario = player
        self.stage_level = 1

    def draw(self):
        # GameState Background
        if (self.mario != None):
            rect = (50 * (self.stage_level - 1), 0, get_canvas_width() + 100 * self.stage_level, get_canvas_height())
            (x, y) = (get_canvas_width() // 2, get_canvas_height() // 2)
            (mx, my) = self.mario.pos
            (dx, dy) = (x - mx, y - my)
            self.image.clip_draw(*rect, x + 0.1 * dx, y)
        # TitleState Background
        else:                   
            (w, h) = (get_canvas_width(), get_canvas_height())
            rect = (200, 80, w, h)
            pos = (0, 0)
            self.image.clip_draw_to_origin(*rect, *pos)

    def update(self):
        pass

    def set_stage_level(self, level):
        self.stage_level = level