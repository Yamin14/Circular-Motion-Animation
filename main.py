import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import*
from kivy.uix.widget import Widget
from math import *

class Animation(Widget):
	def __init__(self, **kwargs):
		super(Animation, self).__init__(**kwargs)
		
		#colours
		self.red = (1, 0, 0, 1)
		self.green = (0, 1, 0, 1)
		self.blue = (0, 0, 1, 1)
		self.yellow = (1, 1, 0, 1)
		self.cyan = (0, 1, 1, 1)
		self.black = (0, 0, 0, 1)
		self.white = (1, 1, 1, 1)
		
		#background
		with self.canvas:
			Color(rgba=self.red)
			Rectangle(size=(720, 1440))
			
		#circle
			self.x, self.y = 100, 700
			self.speed = 0
			self.inc = 0
			Color(rgba=self.yellow)
			self.circle = Ellipse(size=(50, 50), pos=(self.x, self.y))
		
		Clock.schedule_interval(self.play, 0)
		
	def play(self, dt):
		#moving in a circle
		self.x = 320 + (220 * sin(radians(self.speed)))
		self.y = 700 + (220 * cos(radians(self.speed)))
		
		self.speed += self.inc
		self.inc += 0.05
		self.circle.pos = (self.x, self.y)
		
class MyApp(App):
	def build(self):
		return Animation()
		
if __name__ == "__main__":
	MyApp().run()
