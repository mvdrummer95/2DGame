import kivy 
kivy.require('1.10.0')
from kivy import app
from kivy.uix import button as button
from kivy.core.window import Window
from kivy import Config
from kivy import clock
from kivy import app

clock.max_iteration = 20
Config.set('graphics', 'multisamples', '0')
x = 2


b1 = button.Button(pos_hint={'x': 0, 'center_y': .5})
b2 = button.Button(pos_hint={'right': 1, 'center_y': .5})
#class TestApp(app):
#    pass

while x > 1:
	Window.fullscreen = True

#if __name__ == '__main__':
#    Testapp
