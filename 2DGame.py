"""RollerGame.py."""
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder

Builder.load_file('2DGame.kv')


class Controls(FloatLayout):
    pass


class RollerApp(App):
    """Main app."""
    def build(self):
        """."""
        return Controls()


if __name__ == '__main__':
    RollerApp().run()
