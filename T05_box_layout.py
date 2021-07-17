from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (360, 600)


class LayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        layout1 = BoxLayout(spacing=10)
        layout2 = BoxLayout()
        btn1 = Button(text="Button 1")
        btn2 = Button(text="Button 2")
        btn3 = Button(text="Button 3")
        btn4 = Button(text="Button 4")
        btn5 = Button(text="Button 5")
        btn6 = Button(text="Button 6")
        layout1.add_widget(btn1)
        layout1.add_widget(btn2)
        layout1.add_widget(btn3)
        layout2.add_widget(btn4)
        layout2.add_widget(btn5)
        layout2.add_widget(btn6)
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        return layout


LayoutApp().run()
