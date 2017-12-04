"""RollerGame.py."""
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder

Builder.load_file('2DGame.kv')



class RollerApp(App):
    """Main app."""
    def build(self):
        """."""
        return Controls()



class Controls(FloatLayout):
    def Test_Function1(self):
        self.ids['1'].background_color = 0, 0.0, 0.0, 1.0
        self.ids['2'].background_color = 0, 0.0, 0.0, 1.0
        self.ids['3'].background_color = 0, 0.0, 0.0, 1.0
        self.ids['4'].background_color = 0, 0.0, 0.0, 1.0
    def Test_Function2(self):
        self.ids['1'].background_color = 0, 0.0, 1.0, 1.0
        self.ids['2'].background_color = 0, 0.0, 1.0, 1.0
        self.ids['3'].background_color = 0, 0.0, 1.0, 1.0
        self.ids['4'].background_color = 0, 0.0, 1.0, 1.0
    def Test_Function3(self):
        self.ids['1'].background_color = 0, 1.0, 0.0, 1.0
        self.ids['2'].background_color = 0, 1.0, 0.0, 1.0
        self.ids['3'].background_color = 0, 1.0, 0.0, 1.0
        self.ids['4'].background_color = 0, 1.0, 0.0, 1.0
    def Test_Function4(self):
        self.ids['1'].background_color = 1, 0.0, 0.0, 1.0
        self.ids['2'].background_color = 1, 0.0, 0.0, 1.0
        self.ids['3'].background_color = 1, 0.0, 0.0, 1.0
        self.ids['4'].background_color = 1, 0.0, 0.0, 1.0
    pass


if __name__ == '__main__':
    RollerApp().run()
