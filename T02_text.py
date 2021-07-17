from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class TextApp(App):
    def build(self):
        label = Label(text="Hi There",
                      color=(1, 0, 0, 1),
                      font_size="20sp",
                      bold=True, italic=True)
        return label


TextApp().run()
