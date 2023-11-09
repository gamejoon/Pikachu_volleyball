from pico2d import load_image
from random import randint
import game_framework

class Cloud:
    image = None
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 48
        self.height = 24
        self.x = randint(self.screen_width - 500, self.screen_width - 1)
        self.y = randint(self.screen_height // 2, self.screen_height)
        self.speed = randint(1, 3)
        self.speed_pps = self.func_speed_pps()
        self.sizediff = randint(0, 10)
        if Cloud.image == None:
            Cloud.image = load_image("cloud.png")
    
    def update(self):
        self.x += self.speed_pps * game_framework.frame_time
        self.sizediff = self.func_frame_per_sizediff()
        if self.x - (self.width + self.func_sizediff()) // 2 > self.screen_width:
            self.x = self.screen_width - 500
            self.y = randint(self.screen_height // 2, self.screen_height)
            self.speed = randint(1, 3)
            self.func_speed_pps()

    def draw(self):
        self.image.draw(self.x, self.y, self.width + self.func_sizediff(), self.height + self.func_sizediff())
        # self.size + 2 * (5 - (|5 - (0 ~ 10)|))
    
    def func_sizediff(self):
        return 2 * (5 - abs(int(self.sizediff) - 5))    
    
    def func_speed_pps(self):
        pixel_per_meter = (10.0 / 0.5) # 10pixel 50cm
        speed_mps = self.speed
        speed_pps = (speed_mps * pixel_per_meter)
        return speed_pps
    
    def func_frame_per_sizediff(self):
        time_per_sizediff = 0.5
        sizediff_per_time = 1.0 / time_per_sizediff
        frame_per_sizediff = 11
        return (self.sizediff + sizediff_per_time * frame_per_sizediff * game_framework.frame_time) % 11