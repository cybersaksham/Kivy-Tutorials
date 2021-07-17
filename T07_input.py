from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

Window.size = (360, 600)


class InputApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=40,
                            row_force_default=True,
                            row_default_height=40)
        self.wid = TextInput(text="Width")
        self.ht = TextInput(text="Height")
        submit = Button(text="Submit", on_press=self.submit)
        layout.add_widget(self.wid)
        layout.add_widget(self.ht)
        layout.add_widget(submit)
        return layout

    def submit(self, _):
        print(f"{self.wid.text}, {self.ht.text}")


InputApp().run()
