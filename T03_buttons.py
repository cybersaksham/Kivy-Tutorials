from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class BtnApp(App):
    def build(self):
        btn = Button(text="Hi There",
                     size_hint=(0.1, 0.1),
                     pos_hint={'center_x': 0.5, 'center_y': 0.8},
                     on_press=self.press,
                     on_release=self.release)
        return btn

    @staticmethod
    def press(_):
        print("Press")

    @staticmethod
    def release(_):
        print("Release")


BtnApp().run()
