from kivy.app import App
from kivy.uix.widget import Widget


class WindowGame(Widget):
    pass


class WindowApp(App):
    def build(self):
        return WindowGame()


WindowApp().run()
