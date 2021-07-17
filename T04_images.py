from kivy.app import App
from kivy.uix.image import Image, AsyncImage


class ImageApp(App):
    def build(self):
        # img = Image(source="cute.png")
        img = AsyncImage(source="https://www.freeiconspng.com/thumbs/cute-icon-png/cute-twitter-icon-png-0.png")
        return img


ImageApp().run()
